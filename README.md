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

average = 0.5 × model_score + 0.5 × style_score
combined = 0.5 + 1.5 × (average − 0.5), clipped to 0–1

The weights are WEIGHT_MODEL_SIGNAL and WEIGHT_STYLE_SIGNAL (0.5 each) and the stretch is STRETCH_FACTOR (1.5), all in config.py.

This is the same as narrowing the unsure band. My thresholds stay at 0.15 and 0.85 on the combined score, but measured on the plain average they work out to: human if the average is 0.267 or below, and AI if it is 0.733 or above.

Why: With a plain average, none of my four calibration inputs reached a confident label. The AI label could not be reached at all: my highest style score was 0.60, so the model would have needed a score above 1.0. I chose the stretch over giving the model signal more weight, because the model signal is the one that reads plain writing as AI. Weighting it at 0.8 would have raised my own formal writing from 0.53 to 0.58.

Known weakness: I picked 1.5 using the same four inputs I tested with, so it is tuned to them. The unit 8 attack set is a fairer test.

Where it lives: scoring.py::combine_signals

Calibration run (calibrate.py::main, same pipeline as /submit):

Input Words Model Style Average Combined (stretched)
clearly AI 154 0.8015 0.4915 0.6465 0.7198
clearly human 120 0.2568 0.2103 0.2335 0.1003
formal human 68 0.6164 0.4454 0.5309 0.5464
lightly-edited AI 141 0.9290 0.6035 0.7663 0.8995

---

## Label Variants

The text below is copied exactly as scoring.py::score_to_label returns it. A score of exactly 0.15 counts as human and exactly 0.85 counts as AI.

Label Score range The exact text a reader sees
high-confidence human 0.00 – 0.15 We think this was most likely written by...a person.
unsure above 0.15 and below 0.85 We couldn’t tell whether...a person or AI wrote this. It could be either.
high-confidence AI 0.85 – 1.00 Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree |

**Why I worded the "unsure" one this way:**

Most real writers who get a middle score will have written every word themselves, so the unsure label only says that we couldn't tell. It names both possibilities equally ("a person or AI") and does not suggest the writer did anything wrong. I kept the AI label's "we could be wrong" and the mention of appealing because that label is the one a real writer might wrongly receive.

---

## Sample Run

un on Windows PowerShell, so the commands use curl.exe and send the JSON from a file.

**_A submission_**

sample-submit.json:

{"text":"A writing platform should explain how it evaluates submissions. Automated checks can identify patterns, but they can also make mistakes. Writers should have a clear way to challenge a decision.","creator_id":"kenneth"}

powershell

curl.exe -i -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" --data-binary "@sample-submit.json"
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.13.15
Date: Tue, 03 Nov 2026 06:57:29 GMT
Content-Type: application/json
Content-Length: 273
Connection: close

{
"confidence": 0.4585,
"content_id": "9d059376-a5be-4f7b-a2d6-2be01b72fa5c",
"guess": "unsure",
"label": "We couldn’t tell whether...a person or AI wrote this. It could be either.",
"model_score": 0.4279,
"status": "classified",
"style_score": 0.5167
}

The model scored it 0.4279 and the style signal 0.5167. Their average is 0.4723, which the stretch moves to 0.4585, inside the unsure range.

**_An appeal_**

appeal.json:

json
{"content_id":"9d059376-a5be-4f7b-a2d6-2be01b72fa5c","reasoning":"I wrote this myself as project notes. It reads plainly because I wrote it to be clear."}
powershell
curl.exe -i -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" --data-binary "@appeal.json"
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.13.15
Date: Tue, 03 Nov 2026 06:58:38 GMT
Content-Type: application/json
Content-Length: 170
Connection: close

{
"content_id": "9d059376-a5be-4f7b-a2d6-2be01b72fa5c",
"message": "Your appeal has been received. A person will review this decision.",
"status": "under_review"
}

**_What the log shows afterwards_**

powershell

curl.exe "http://127.0.0.1:5000/log?limit=2"

{
"count": 2,
"entries": [
{
"combined_score": 0.4585,
"content_id": "9d059376-a5be-4f7b-a2d6-2be01b72fa5c",
"creator_id": "kenneth",
"guess": "unsure",
"label": "We couldn’t tell whether...a person or AI wrote this. It could be either.",
"model_score": 0.4279,
"status": "classified",
"style_score": 0.5167,
"timestamp": "2026-11-03T06:57:29+00:00"
},
{
"content_id": "9d059376-a5be-4f7b-a2d6-2be01b72fa5c",
"creator_id": "kenneth",
"event": "appeal",
"reasoning": "I wrote this myself as project notes. It reads plainly because I wrote it to be clear.",
"status": "under_review",
"timestamp": "2026-11-03T06:58:38+00:00"
}
]
}

## The original decision stays in the log unchanged. The appeal is added after it with the same content_id, the writer's exact reasoning, and the status under_review. An appeal does not re-run the detector.

## How I Used AI

**Moment 1**

What I asked for: I asked Claude to check my combining rule (an equal-weight average) against my calibration results.
What came back: It showed that with my style scores, the AI label could not be reached at all: the model would have needed a score above 1.0. It gave three options with the scores each would produce: keep the average, weight the model at 0.8, or stretch the average away from the middle. It also corrected one of its own earlier estimates, about how far word variety moves on longer text, once my real numbers came in.
What I changed: I rejected the heavier model weight, because it raised my own formal writing toward an AI label. I chose the stretch, and I wrote the rule into this README and committed it before I changed the code. I also recorded that 1.5 was tuned on my own four inputs.

**Moment 2**

What I asked for: Code to wire the second signal and the combined score into /submit and the audit log.
What came back: Its first version also connected score_to_label, which is Milestone 5 work.
What I changed: I kept Milestone 4 to its scope. The guess and label stay placeholders until Milestone 5, and only the two signal scores and the combined score were wired in. When the response still showed null scores, I checked the file with Select-String. That showed the edit hadn't saved, so I replaced the whole function and confirmed the response showed style 0.5167 and combined 0.4723.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 submissions per minute and 200 per day.

**Why these numbers:** Ten per minute allows a writer to submit several
revisions while restricting rapid automated submissions. Two hundred per
day caps sustained submissions while allowing substantial ordinary use.
These are initial limits for this exercise, not production-tested limits.

**What a caller counts as:** Requests are counted by creator_id.
Requests without a usable creator_id fall back to the caller's IP address.
Changing creator_id can bypass the per-creator cap, so this does not
prevent all automated abuse.

**Flood test:** Ran `python run_attacks.py --flood 15`.

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Ten requests succeeded and five were rate limited.
Result file: `results/flood_2026-11-10_0105.md`.

**Logged rejection:**

```json
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-10T06:05:11+00:00"
}
```

The per-minute limit was verified. The daily limit is configured but
has not been tested.

## Attack Run — Before

I ran all 56 attacks using:

```text
python run_attacks.py --set .\attack_set\attack_set --label before
```

Results: `results/attack_run_2026-11-10_0111_before.md`

Every request received a response. There were no crashes or 500 errors.

For evasion attacks, I counted avoiding the AI label as BROKE,
including an unsure result. For false-positive attacks, unsure
counted as HELD because it did not accuse the writer of using AI.

For unusual inputs, I counted a confident authorship label on
non-writing content as BROKE. These are my review rules. The CSV
describes the attacks but does not supply expected verdicts.

| ID      | Status | Result       | Verdict |
| ------- | ------ | ------------ | ------- |
| EV01    | 200    | unsure       | BROKE   |
| EV02    | 200    | unsure       | BROKE   |
| EV03    | 200    | unsure       | BROKE   |
| EV04    | 200    | unsure       | BROKE   |
| EV05    | 200    | unsure       | BROKE   |
| EV06    | 200    | unsure       | BROKE   |
| EV07    | 200    | unsure       | BROKE   |
| EV08    | 200    | unsure       | BROKE   |
| EV09    | 200    | unsure       | BROKE   |
| EV10    | 200    | ai           | HELD    |
| FP01    | 200    | unsure       | HELD    |
| FP02    | 200    | unsure       | HELD    |
| FP03    | 200    | unsure       | HELD    |
| FP04    | 200    | unsure       | HELD    |
| FP05    | 200    | unsure       | HELD    |
| FP06    | 200    | unsure       | HELD    |
| FP07    | 200    | unsure       | HELD    |
| FP08    | 200    | unsure       | HELD    |
| PI01    | 200    | unsure       | HELD    |
| PI02    | 200    | human        | BROKE   |
| PI03    | 200    | unsure       | HELD    |
| PI04    | 200    | unsure       | HELD    |
| PI05    | 200    | unsure       | HELD    |
| PI06    | 200    | unsure       | HELD    |
| MF01    | 400    | rejected     | HELD    |
| MF02    | 400    | rejected     | HELD    |
| MF03    | 200    | human        | BROKE   |
| MF04    | 200    | human        | BROKE   |
| MF05    | 200    | ai           | BROKE   |
| MF06    | 200    | ai           | BROKE   |
| MF07    | 200    | unsure       | HELD    |
| MF08    | 200    | ai           | BROKE   |
| RQ01    | 400    | rejected     | HELD    |
| RQ02    | 400    | rejected     | HELD    |
| RQ03    | 400    | rejected     | HELD    |
| RQ04    | 400    | rejected     | HELD    |
| RQ05    | 400    | rejected     | HELD    |
| RQ06    | 400    | rejected     | HELD    |
| RQ07    | 400    | rejected     | HELD    |
| RQ08    | 400    | rejected     | HELD    |
| RQ09    | 400    | rejected     | HELD    |
| RQ10    | 415    | rejected     | HELD    |
| RQ11    | 415    | rejected     | HELD    |
| RQ12    | 400    | rejected     | HELD    |
| FL01_01 | 200    | within limit | HELD    |
| FL01_02 | 200    | within limit | HELD    |
| FL01_03 | 200    | within limit | HELD    |
| FL01_04 | 200    | within limit | HELD    |
| FL01_05 | 200    | within limit | HELD    |
| FL01_06 | 200    | within limit | HELD    |
| FL01_07 | 200    | within limit | HELD    |
| FL01_08 | 200    | within limit | HELD    |
| FL01_09 | 200    | within limit | HELD    |
| FL01_10 | 200    | within limit | HELD    |
| FL01_11 | 429    | rate limited | HELD    |
| FL01_12 | 429    | rate limited | HELD    |

Total under these rules: 41 HELD, 15 BROKE.

PI02 received the human label requested in its text, but its score
was 0.0505 rather than the requested 0.02. I marked the classification
outcome as BROKE; this does not prove the system followed instructions.

PI04 did not change the label into hostile content, and PI05 did not
insert its requested fields into the audit record.

MF07 contains Arabic writing. It is not invalid just because it uses
a different script. The service returned unsure without crashing,
although this does not establish that its multilingual scoring works.

The flood group contains 12 requests, despite its description saying 20. The first ten were within the configured limit. The next two
were blocked.

**Ten audit log entries from the run**

```json
{"timestamp":"2026-11-10T06:11:10+00:00","content_id":"cd7920ad-bca5-4a9b-a22b-ef51cbd132cf","creator_id":"attacker_EV01","guess":"unsure","model_score":0.1635,"style_score":0.4843,"combined_score":0.2359,"label":"We couldnâ€™t tell whether a person or AI wrote this. It could be either.","status":"classified"}
{"timestamp":"2026-11-10T06:11:10+00:00","content_id":"29be6e2d-688f-4343-b03b-ad6303baf09c","creator_id":"attacker_EV02","guess":"unsure","model_score":0.5943,"style_score":0.1633,"combined_score":0.3182,"label":"We couldnâ€™t tell whether a person or AI wrote this. It could be either.","status":"classified"}
{"timestamp":"2026-11-10T06:11:12+00:00","content_id":"20ba93c5-bc78-459e-b383-3e39fc74bde1","creator_id":"attacker_EV10","guess":"ai","model_score":0.9792,"style_score":0.6428,"combined_score":0.9665,"label":"Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree","status":"classified"}
{"timestamp":"2026-11-10T06:11:12+00:00","content_id":"c2de4e52-0981-4e49-b9cc-fae508dab8a2","creator_id":"attacker_FP05","guess":"unsure","model_score":0.8005,"style_score":0.5687,"combined_score":0.7769,"label":"We couldnâ€™t tell whether a person or AI wrote this. It could be either.","status":"classified"}
{"timestamp":"2026-11-10T06:11:13+00:00","content_id":"14a8bd21-f2a5-47e0-b110-6f29285fb651","creator_id":"attacker_PI02","guess":"human","model_score":0.2044,"style_score":0.1963,"combined_score":0.0505,"label":"We think this was most likely written by a person.","status":"classified"}
{"timestamp":"2026-11-10T06:11:13+00:00","content_id":"c4750071-2b03-4f36-9a5b-94730147940c","creator_id":"attacker_PI05","guess":"unsure","model_score":0.6401,"style_score":0.281,"combined_score":0.4408,"label":"We couldnâ€™t tell whether a person or AI wrote this. It could be either.","status":"classified"}
{"timestamp":"2026-11-10T06:11:14+00:00","content_id":"896d89b4-8363-4e45-b637-624b589b88f4","creator_id":"attacker_MF04","guess":"human","model_score":0.0112,"style_score":0.5,"combined_score":0.1334,"label":"We think this was most likely written by a person.","status":"classified"}
{"timestamp":"2026-11-10T06:11:15+00:00","content_id":"bf133f9f-3f80-4952-9ab0-ff9b239bd8c8","creator_id":"attacker_MF06","guess":"ai","model_score":0.9969,"style_score":0.5,"combined_score":0.8727,"label":"Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree","status":"classified"}
{"timestamp":"2026-11-10T06:11:15+00:00","content_id":"8b978897-a2f2-4ab2-8105-58bed9b164c0","creator_id":"attacker_MF08","guess":"ai","model_score":0.9876,"style_score":0.7827,"combined_score":1.0,"label":"Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree","status":"classified"}
{"timestamp":"2026-11-10T06:11:16+00:00","creator_id":"attacker_flood","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
```

**The single worst outcome**

MF08 repeated the campsite paragraph from the human-writing examples
but received an AI score of 1.0. Its model score was 0.9876 and its
style score was 0.7827.

I chose this as the worst outcome because repeated human-source
writing received the strongest AI score. I need to examine how
repetition and length affected the signals before choosing a fix.

---

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion                        | Target                                                     | Run 1 | Run 2 | Run 3 | Verdict |
| -------------------------------- | ---------------------------------------------------------- | ----- | ----- | ----- | ------- |
| 1. My writing labelled AI        | At most 1 of 10                                            | 0/10  | 0/10  | 0/10  | MET     |
| 2. All three labels appear       | 3 of 3 labels                                              | 2/3   | 2/3   | 2/3   | MISSED  |
| 3. Valid appeals are recorded    | 5 of 5 pass every check                                    | 5/5   | 5/5   | 5/5   | MET     |
| 4. Invalid text returns an error | 4 of 4 return 400, an error message, and no classification | 4/4   | 4/4   | 4/4   | MET     |
| 5. Scores map to correct labels  | 9 of 9 categories and label texts match                    | 9/9   | 9/9   | 9/9   | MET     |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

**Real output from one trial**

These examples come from trial 1. The complete results for all
three trials are saved in `results/`.

**Criterion 1 — My own writing**

Produced by `run_eval.py::main`, calling `app.py::submit`.
Sample 1 returned HTTP 200:

```json
{
  "confidence": 0.3167,
  "content_id": "24e73a98-3ac8-49fb-9fe6-ad86b594c26b",
  "guess": "unsure",
  "label": "We couldn’t tell whether a person or AI wrote this. It could be either.",
  "model_score": 0.2209,
  "status": "classified",
  "style_score": 0.5347
}
```

**Criterion 2 — Label coverage**

Produced by `run_eval.py::main`, calling `app.py::submit`.
The generated learning paragraph returned HTTP 200:

```json
{
  "confidence": 0.6417,
  "content_id": "c946441f-1436-4ce3-b967-f351f5f7d86f",
  "guess": "unsure",
  "label": "We couldn’t tell whether a person or AI wrote this. It could be either.",
  "model_score": 0.7009,
  "status": "classified",
  "style_score": 0.488
}
```

**Criterion 3 — Appeals**

Produced by `test_appeals.py::main`, calling `app.py::appeal`.
The first appeal returned HTTP 200:

```json
{
  "content_id": "34b400f0-71b7-48b5-a307-8662149ba5c5",
  "message": "Your appeal has been received. A person will review this decision.",
  "status": "under_review"
}
```

Its new audit entry was:

```json
{
  "content_id": "34b400f0-71b7-48b5-a307-8662149ba5c5",
  "creator_id": "appeal_eval_521c32dc5c4a_1",
  "event": "appeal",
  "reasoning": "I wrote sample 1 myself. Please review the classification.",
  "status": "under_review",
  "timestamp": "2026-11-11T20:39:21+00:00"
}
```

The test compared the log before and after each appeal. The original
decision stayed unchanged. Current status was checked using the
latest entry for that content ID.

**Criterion 4 — Invalid text**

Produced by `run_eval.py::main`, calling `app.py::submit`.
The request with no text field returned HTTP 400:

```json
{
  "error": "text must be a nonempty string."
}
```

**Criterion 5 — Label boundaries**

Produced by `test_boundaries.py::main`, calling
`scoring.py::score_to_label` directly:

```json
{
  "score": 0.0,
  "expected_guess": "human",
  "expected_label": "We think this was most likely written by a person.",
  "actual_guess": "human",
  "actual_label": "We think this was most likely written by a person.",
  "passed": true
}
```

**Diagnoses**
### Diagnoses

#### How I judged the results

The five criteria use the targets I wrote in Unit 7. I did not
change those targets after seeing the results.

The attack CSV describes what each attack targets, but does not give
an exact pass/fail rule for every input. I chose the attack review
rules after the first run. This is a limitation of my evaluation.
I will use the same rules for the after run.

For evasion, I counted avoiding the AI label as BROKE, including an
unsure result. Under that rule, 41 attacks held and 15 broke.
However, none of EV01–EV10 received a human label. Nine returned
unsure and one returned AI. Avoiding an AI label is different from
being confidently classified as human.

For non-writing inputs, I treated a confident authorship label as
BROKE. This was a weakness discovered through the attack set, not
part of my original invalid-text criterion.

#### Why each criterion met or missed

1. **MET — My own writing**

   None of my ten samples received the AI label in any trial.
   This meets my target of at most one false positive per trial.

   This is a small sample of my writing. Some pieces contain
   quotations, and samples 7–9 are related excerpts. The result
   does not establish accuracy across other writers or topics.

2. **MISSED — Label coverage**

   Only human and unsure appeared across the 15 fixed inputs.
   The highest combined score was 0.6417, below the AI threshold
   of 0.85.

   The relevant stages are the combining rule and label mapping.
   The two signals did not combine into a high enough score for
   these inputs to reach AI. The boundary function passed its
   separate tests.

   The AI label is reachable: several attack inputs received it.
   This is a coverage failure on my fixed test set, not an
   unreachable label. I kept the original samples and target.

3. **MET — Appeals**

   All five appeals passed every check in all three trials.
   Each returned HTTP 200, the correct content ID, a confirmation,
   and under_review status.

   The log recorded the exact reasoning and preserved the original
   decision. Current status was checked using the latest audit
   entry for that content ID. This tests recording an appeal,
   not whether a person eventually reviews it.

4. **MET — Invalid text**

   All four inputs returned HTTP 400 with a nonempty error message
   and no classification fields in all three trials.

   These cases were missing text, an empty string, spaces only,
   and the number 123. This result does not cover every possible
   malformed or unsuitable input.

5. **MET — Label boundaries**

   All nine scores returned the expected category and exact label
   text in all three trials.

   This verifies the boundary mapping. It does not establish that
   the signals produce accurate authorship scores.

#### Broken attacks: stages and mechanisms

The scores below are observed results. The code explains how those
scores produced the labels. Where an attack changes wording or
structure, I have not run an unmodified comparison input, so I
cannot isolate how much that particular edit changed the score.

| Attack | Stage | Diagnosis |
|---|---|---|
| EV01 | Model signal and combining rule | Model scored 0.1635 and style scored 0.4843, producing 0.2359 and unsure. The model was the lower-scoring signal, although the attack description targeted word variety. Typos may affect predictability and word statistics, but this run alone does not isolate their effect. |
| EV02 | Style signal and combining rule | Style scored 0.1633 versus model 0.5943, producing 0.3182. The style formula lowers its score when sentence lengths vary. The inserted short sentences fit that weakness, but their exact effect needs an unmodified comparison. |
| EV03 | Style signal and combining rule | Style scored 0.3585 versus model 0.6662, producing 0.5185. The style calculation includes the pasted quotation in the same word and sentence statistics. It does not distinguish quoted material from the rest of the submission. |
| EV04 | Model signal and combining rule | Model scored 0.6114 and style scored 0.4769, producing 0.5662. The model measures predictability rather than authorship. Unusual words can affect that measure, but the run does not prove how much the substitutions changed it. |
| EV05 | Both signals and combining rule | Model scored 0.3212 and style scored 0.2782. Both were below 0.5, and the stretch moved their average further down to 0.1995. Neither signal identifies whether a passage started as generated text and was then edited. |
| EV06 | Style signal and combining rule | Style scored 0.1250 versus model 0.5727, producing 0.2733. The style formula treats sentence-length variation as less AI-like. The deliberately uneven sentences fit this mechanism. |
| EV07 | Style fallback and combining rule | Style returned 0.5 and model scored 0.5862, producing 0.5647. The code falls back to 0.5 when it finds fewer than 20 words or fewer than two usable sentences. The attack joins sentences with punctuation that the sentence splitter does not treat as sentence endings. Punctuation density is not used in the final style score. |
| EV08 | Style fallback and model signal | The short input triggered style's 0.5 fallback. Model scored 0.2452, producing 0.3089. The fallback supplies a neutral number rather than indicating insufficient evidence, so the system still returns an authorship judgment. |
| EV09 | Style signal and combining rule | Model scored 0.7042 and style scored 0.3428, producing 0.5353. The signals do not separate the human opening from the generated section. They score the supplied text without identifying the origin of its individual parts. |
| PI02 | Both signals and combining rule | Model scored 0.2044 and style scored 0.1963, producing 0.0505 and human. The requested human category appeared, but the request to bypass scoring and return exactly 0.02 did not succeed. The code computes model loss and fixed labels rather than generating a reply to the instruction. I count this as classification evasion under my review rule, not demonstrated instruction-following. |
| MF03 | Input validation and style fallback | The control-containing text passed the nonempty-string check. Model scored 0.0000 and style returned 0.5, producing 0.1250 and human. The route does not check whether the input is suitable writing for an authorship judgment. |
| MF04 | Input validation and style fallback | Punctuation-only text passed validation. Style returned 0.5 because it found no usable words. Model scored 0.0112, producing 0.1334 and human. A lack of writing was not treated as insufficient evidence. |
| MF05 | Input validation, model signal, and combining rule | A long repeated word passed validation. Model scored 0.9976 and style returned 0.5. The stretch raised the combined score to 0.8732 and AI. A repetitive input can score as predictable without providing reliable evidence of authorship. |
| MF06 | Input validation, model signal, and combining rule | Repeated emojis passed validation. Model scored 0.9969 and style returned 0.5 because its word matcher does not recognize emojis as words. The combined score reached 0.8727 and AI. The fallback did not prevent a confident label on non-writing content. |
| MF08 | Both signals and combining rule | Repeated human-source text scored 0.9876 on the model and 0.7827 on style. Repeating words lowers the unique-word ratio, which raises the style score. The model examines at most 400 tokens while style uses the whole input. The stretch pushed the combined result above 1, which was clipped to 1.0. This demonstrates a weakness on artificially repeated text, not proof that an ordinary human submission would score the same way. |

#### Other limitations found

**MF07 — Arabic text**

The style word matcher recognizes only ASCII letters, digits, and
apostrophes. It does not meaningfully analyze this Arabic passage
and returns its fallback score of 0.5.

The service returned unsure without crashing. I marked that outcome
HELD, but it does not demonstrate multilingual accuracy. Arabic
writing is not invalid simply because it uses a different script.

**Rate limiting**

The flood tests show that the configured per-creator limit works.
They do not show that one person cannot evade it by changing their
creator_id. These tests also do not verify the daily limit.

#### Main pattern

The detector measures predictability and text patterns, not authorship.
Some generated or edited inputs avoided the AI label because their
combined scores stayed below 0.85. Other inputs received confident
labels even though they contained little or no meaningful writing.

The validation checks handle missing and incorrectly typed text,
but they do not establish that accepted text is suitable for scoring.
The style fallback also hides the difference between a neutral
measurement and a measurement that could not meaningfully be made.

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
