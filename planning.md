# Milestone 1: Planning

## 1. How a submission moves through the app

1. The writer sends their text and creator_id to POST /submit.
2. The app checks that both fields are strings and are not blank.
3. The app gives the submission a unique content_id so we can
   find it later if the writer appeals.
4. detector.py checks the text using the local model and returns
   the first signal.
5. stylometry.py checks sentence lengths and word variety and
   returns the second signal.
6. The app combines both signals into one score and chooses
   an AI, human, or unsure label.
7. The app saves the IDs, time, scores, decision, and status in
   the audit log. It returns the result as JSON so a website
   can show the label.

## 2. My two signals

### detector.py

This is the signal provided with the project. According to the
lecture, it checks how predictable the writing is to the model.

Some AI writing may follow predictable patterns, so this could
help us make a guess. But human writing can be predictable too.
It cannot tell who actually wrote the text.

### stylometry.py

I will measure how much the sentence lengths vary and how many
different words the writer uses compared with the total word count.

These measurements might help identify repetitive or uniform
writing. But a person can repeat words on purpose, especially
in a poem. AI can also write with variety. Very short text will
be hard to judge because there is not much to measure.

The two signals check different things, but both can be wrong.

## 3. What happens if we wrongly flag a real writer?

For my starting plan, a higher score means the text looks more
AI-generated. It does not prove that AI wrote it.

My proposed ranges are:

- 0 to 0.15: high-confidence human.
- Above 0.15 and below 0.85: unsure.
- 0.85 to 1: high-confidence AI.

I chose a wide unsure range because I want to be careful about
wrongly accusing a real writer. These are starting choices,
not results from testing.

For example, a person writes a poem with repeated words and
similar sentence lengths. Imagine the app gives it 0.88 and
labels it AI-generated, even though the person wrote it.

The label would say:

"Our checks suggest this writing may be AI-generated, but we
could be wrong. You can appeal if you disagree."

The writer sends the content_id and their explanation to
POST /appeal. The app records the appeal, changes the status
to under_review, and confirms that it received the appeal.

The original scores and decision stay in the log. An appeal
does not automatically change the guess or run the detector again.

## 4. My endpoints

Both endpoints receive and return JSON.
Requests must use Content-Type: application/json.

### POST /submit

What goes in:

| Field      | Type   | Meaning                               |
| ---------- | ------ | ------------------------------------- |
| text       | String | The writing to check; cannot be blank |
| creator_id | String | The writer's ID; cannot be blank      |

What comes back on success (HTTP 200):

| Field      | Type   | Meaning                                      |
| ---------- | ------ | -------------------------------------------- |
| content_id | String | Unique ID for this submission                |
| guess      | String | ai, human, or unsure                         |
| confidence | Number | Score from 0 to 1; higher means more AI-like |
| label      | String | The explanation shown to the reader          |
| status     | String | classified                                   |

Here, confidence means the combined AI-evidence score.
It is not a proven percentage chance that AI wrote the text.

### POST /appeal

What goes in:

| Field      | Type   | Meaning                                        |
| ---------- | ------ | ---------------------------------------------- |
| content_id | String | The submission being appealed; cannot be blank |
| reasoning  | String | Why the writer disagrees; cannot be blank      |

What comes back on success (HTTP 200):

| Field      | Type   | Meaning                                   |
| ---------- | ------ | ----------------------------------------- |
| content_id | String | The submission being appealed             |
| status     | String | under_review                              |
| message    | String | Confirmation that the appeal was recorded |

The app saves the appeal's time, content_id, and reasoning.
If the writer appeals again, it records the new appeal and
keeps the status as under_review.

### Errors

For both endpoints:

- Return HTTP 400 for broken JSON, a body that is not an object,
  missing fields, wrong field types, or blank required values.
- Blank includes strings containing only spaces.
- Return HTTP 415 if the request is not application/json.
- Return errors as JSON with an error field explaining the problem.

For /appeal, also return HTTP 404 if the content_id does not exist.
