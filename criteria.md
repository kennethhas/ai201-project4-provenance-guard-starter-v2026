# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. _"The
detector is accurate"_ is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. _"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"_ is a criterion.

Under each, write a sentence or two on **why that target**. _"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"_ is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. Limit wrong AI labels on human writing

I will submit the same 10 pieces I wrote myself through
POST /submit in each trial. I will save the texts so someone
else can repeat the test.

In each trial, at most 1 of the 10 may receive the
high-confidence AI label. Human and unsure labels do not
count as false positives.

**Why this target:**

The detector and style checks can mistake predictable or
repetitive human writing for AI. I allow one mistake in this
small test, but want to keep false accusations low because
they can damage a writer's trust.

## 2. All three labels can appear

I will save a fixed set of 15 texts: 5 human-written,
5 AI-generated, and 5 AI-generated texts that I edit myself.
I will document where each text came from and submit the
same set through POST /submit in each trial.

In each trial, the human, AI, and unsure labels must each
appear at least once across the 15 responses.

This checks label coverage. It does not require edited AI
text to receive the unsure label or prove the labels are correct.

**Why this target:**

My thresholds leave a wide unsure range, from above 0.15
to below 0.85. I want to check that the signals can still
produce scores that reach both other labels. Always returning
unsure would avoid accusations without making useful distinctions.

## 3. Valid appeals are recorded

In each trial, I will create five submissions and send one
POST /appeal request for each returned content_id.
Each appeal will include a nonempty reasoning string.

All 5 appeals must:

- Return HTTP 200 with the correct content_id, status
  under_review, and a nonempty confirmation message.
- Change the corresponding submission's status to under_review.
- Record the exact reasoning and correct content_id in the
  audit log, while preserving the original decision record.

I will check the responses and audit records to verify this.

**Why this target:**

Both signals can wrongly flag a real writer, so the writer
needs a way to challenge the decision. All five appeals must
work because saving an explanation and updating a status
are actions the code controls, even when detection is uncertain.

## 4. Invalid text returns an error

In each trial, I will send four JSON requests to POST /submit,
each with a valid creator_id and one of these text inputs:

- The text field is missing.
- text is an empty string: "".
- text contains only spaces: " ".
- text is a number: 123.

All 4 requests must return HTTP 400 and a JSON object with
a nonempty error message explaining the invalid text.
None may return a classification score or label.

**Why this target:**

Neither signal has valid writing to analyze in these cases.
Returning a score or label would be misleading. A clear
error tells the person sending the request what needs fixing.

## 5. Scores map to the correct labels

In each trial, I will call scoring.py::score_to_label directly
with the nine scores below, without running the detector.

| Score | Expected label category |
| ----- | ----------------------- |
| 0.00  | Human                   |
| 0.14  | Human                   |
| 0.15  | Human                   |
| 0.16  | Unsure                  |
| 0.50  | Unsure                  |
| 0.84  | Unsure                  |
| 0.85  | AI                      |
| 0.86  | AI                      |
| 1.00  | AI                      |

All 9 results must match the expected category and return
the corresponding label text documented in the README.

The rules are:

- Scores from 0 through 0.15 receive the human label.
- Scores above 0.15 and below 0.85 receive the unsure label.
- Scores from 0.85 through 1 receive the AI label.

**Why this target:**

These boundaries control what readers see. A mistake near
0.85 could wrongly turn an unsure result into an AI accusation.
I want to check both boundaries and the ends of the score range.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
