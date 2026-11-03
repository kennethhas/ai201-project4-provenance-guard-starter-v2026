# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a small web service a writing site could use. It takes a piece of writing, makes a guess about whether a person or an AI wrote it, and gives the writer a way to push back.

The path a submission takes:

The writer sends their text. A POST /submit request arrives with text and creator_id as JSON.
The route checks the input (app.py::submit). The request must be JSON (otherwise 415), and both fields must be non-blank strings (otherwise 400 with an error message). Nothing is scored or logged for a bad request.
Signal one reads the text (detector.py::model_signal). A small language model (gpt2) running on my laptop measures how predictable the text is, and turns that into a 0–1 score.
Signal two measures the shape of the text (stylometry.py::style_signal). It looks at how much sentence lengths vary and how often words repeat, and turns that into a 0–1 score.
The two scores become one (scoring.py::combine_signals). Higher always means "more likely AI".
The score becomes a guess and a label (scoring.py::score_to_label): high-confidence human, unsure, or high-confidence AI.
Everything is recorded and returned. The app writes the content id, creator id, both signal scores, the combined score, the guess, the label and the status to logs/audit.jsonl (audit.py), then returns the same result as JSON with a new content_id. The writer can use that id with POST /appeal to say the decision was wrong, which moves the item to under_review.
---

## Signals and Scoring



### Signal one — the model signal

What it measures: How predictable the text is to a language model (gpt2, run locally). The model's perplexity is squashed onto 0–1. Low perplexity, meaning predictable text, gives a high score (more AI-like).

Why that might differ between human and AI writing: An AI writes by repeatedly picking a likely next word, so its text tends to be easy for a model to predict. People make more unusual word choices and turns.

What it can't see: Who actually wrote the text. Predictable is not the same as machine-written. Plain writing, a second-language writer using words they are sure of, or formal writing all look predictable. In my own testing, a formal paragraph I wrote myself scored 0.62 on this signal, leaning AI. Dense writing with rare words can go the other way and look human.

### Signal two — the style signal
What it measures: The shape of the text, without understanding any of it. Two measures go into the score:

Sentence length spread: the standard deviation of sentence lengths divided by the average sentence length. Low spread means sentences march in step.
Type-token ratio (TTR): unique words divided by total words. A low ratio means more repetition.

The score is ((1 − min(spread, 1)) + (1 − TTR)) / 2, so even sentence lengths and repeated words both push it toward 1 (AI-like). I also compute punctuation density, but it is not part of the score.

Why that might differ between human and AI writing: Generated text tends to use even, medium-length sentences and a narrower vocabulary. Human writing is lumpier, with a three-word sentence next to a long one.

What it can't see:

Meaning. Anything that changes the shape without changing the content moves the score: typos, breaking sentences up, pasting in a quotation.
Purposeful repetition. A person can repeat on purpose, for example in a poem.
Length effects. TTR drops as text gets longer, whoever wrote it.
Short text. Under 20 words, or fewer than 2 sentences, it returns a fixed 0.5. So only the model signal decides short submissions.

### The combining rule
The rule: First I take an equal-weight average of the two signals. Then I stretch that average away from the middle, so a score that both signals push in the same direction moves further toward 0 or 1. The result is clipped to stay between 0 and 1.

The numbers:

average  = 0.5 × model_score + 0.5 × style_score
combined = 0.5 + 1.5 × (average − 0.5), clipped to 0–1

The weights are WEIGHT_MODEL_SIGNAL and WEIGHT_STYLE_SIGNAL (0.5 each) and the stretch is STRETCH_FACTOR (1.5), all in config.py.

This is the same as narrowing the unsure band. My thresholds stay at 0.15 and 0.85 on the combined score, but measured on the plain average they work out to: human if the average is 0.267 or below, and AI if it is 0.733 or above.

Why: With a plain average, none of my four calibration inputs reached a confident label. The AI label could not be reached at all: my highest style score was 0.60, so the model would have needed a score above 1.0. I chose the stretch over giving the model signal more weight, because the model signal is the one that reads plain writing as AI. Weighting it at 0.8 would have raised my own formal writing from 0.53 to 0.58.

Known weakness: I picked 1.5 using the same four inputs I tested with, so it is tuned to them. The unit 8 attack set is a fairer test.

Where it lives: scoring.py::combine_signals

Calibration run (calibrate.py::main, same pipeline as /submit):

Input	         Words	 Model	Style	Average	Combined (stretched)
clearly AI	     154	0.8015	0.4915	0.6465	0.7198
clearly human	     120	0.2568	0.2103	0.2335	0.1003
formal human	      68	0.6164	0.4454	0.5309	0.5464
lightly-edited AI	141	0.9290	0.6035	0.7663	0.8995

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label                 | Score range | The exact text a reader sees |
| --------------------- | ----------- | ---------------------------- |
| high-confidence human |             |                              |
| unsure                |             |                              |
| high-confidence AI    |             |                              |

**Why I worded the "unsure" one this way:**

<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- _What I asked for:_
- _What came back:_
- _What I changed:_

**Moment 2**

- _What I asked for:_
- _What came back:_
- _What I changed:_

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
