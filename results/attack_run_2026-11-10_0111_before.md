# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 01:11
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `cd7920ad-bca5-4a9b-a22b-ef51cbd132cf` | unsure | 0.236 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `29be6e2d-688f-4343-b03b-ad6303baf09c` | unsure | 0.318 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2034b72f-e5f8-4655-b01a-916723f0f427` | unsure | 0.518 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `7914e52c-be57-4b7d-a6ff-24155b5c687d` | unsure | 0.566 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3242e6ac-bd0d-4ebb-a225-02f9a29bdda0` | unsure | 0.200 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `315768d2-bdf6-415e-bfac-b8272907e78a` | unsure | 0.273 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `421a1cdc-945a-43ef-a7b4-f942b30c65ed` | unsure | 0.565 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `6038beb2-4b84-4ead-aebf-d8f483829d94` | unsure | 0.309 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ee6d6594-243c-4221-970c-87f2b8cfcd98` | unsure | 0.535 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `20ba93c5-bc78-459e-b383-3e39fc74bde1` | ai | 0.967 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `af9f6d78-661e-41f3-9ce2-cbb776be093c` | unsure | 0.526 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7907ac2e-98dc-43a1-ad74-5623c1b941a4` | unsure | 0.698 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `dd57618a-4b2e-4970-bd0d-cb77b07f91d5` | unsure | 0.710 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `fe1337ee-d94b-4d51-86de-d1e3c63cc545` | unsure | 0.684 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c2de4e52-0981-4e49-b9cc-fae508dab8a2` | unsure | 0.777 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f743b9b3-89f3-4138-bd18-28cc3b0a0738` | unsure | 0.691 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `048619ff-156f-4f6e-b7b2-1b8cabc485b2` | unsure | 0.716 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `ed5c6b91-cd2a-4313-96e8-f0f5f6f1ab73` | unsure | 0.367 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b6e44dba-9110-48ba-a67e-e151a477c9be` | unsure | 0.248 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `14a8bd21-f2a5-47e0-b110-6f29285fb651` | human | 0.051 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `63a8d4aa-b9a0-4c86-8e19-7d76cc7e9f3a` | unsure | 0.476 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `37d42cbf-99d2-45a8-969c-a70b40e949ad` | unsure | 0.403 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c4750071-2b03-4f36-9a5b-94730147940c` | unsure | 0.441 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e7ddc71f-4880-4fd9-8d9a-1c3357621814` | unsure | 0.486 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `980a2485-40ca-497e-9200-b643a3c5c6a7` | human | 0.125 |  |
| MF04 | malformed | text is only punctuation | 200 | `896d89b4-8363-4e45-b637-624b589b88f4` | human | 0.133 |  |
| MF05 | malformed | text is a very long single word | 200 | `52d79caa-61c2-42b5-adbe-f3c858bcf73a` | ai | 0.873 |  |
| MF06 | malformed | text is emoji only | 200 | `bf133f9f-3f80-4952-9ab0-ff9b239bd8c8` | ai | 0.873 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ff23c303-1eeb-483e-a91c-00d2939e1c9c` | unsure | 0.805 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `8b978897-a2f2-4ab2-8105-58bed9b164c0` | ai | 1.000 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 415 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 415 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d87d6d25-f334-4a2e-ad14-4cac8f1f0fe0` | human | 0.146 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1b5866da-c48f-4968-ba2c-429ee83a3bf7` | human | 0.146 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d46a10c-15f6-403e-8042-43348f5ac38c` | human | 0.146 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3fe3b712-fc48-4ed0-aaba-0314ec5d7700` | human | 0.146 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5e87409-3b2c-4f79-ad51-6bc1098bc636` | human | 0.146 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e9434728-8b20-4e80-b78c-7bdc2d5fa9a8` | human | 0.146 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4972aa9b-5d6b-4a18-979b-1e624ef8375a` | human | 0.146 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ba2a09ec-e4ae-4c35-81d9-a078fa67fb86` | human | 0.146 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5e4f7680-6a48-46b4-a04e-9851b2ddc50d` | human | 0.146 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5d30625-c837-4912-9ed3-81f6a05ddcee` | human | 0.146 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "cd7920ad-bca5-4a9b-a22b-ef51cbd132cf",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.2359,
  "model_score": 0.1635,
  "style_score": 0.4843,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "29be6e2d-688f-4343-b03b-ad6303baf09c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3182,
  "model_score": 0.5943,
  "style_score": 0.1633,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "2034b72f-e5f8-4655-b01a-916723f0f427",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5185,
  "model_score": 0.6662,
  "style_score": 0.3585,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "7914e52c-be57-4b7d-a6ff-24155b5c687d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5662,
  "model_score": 0.6114,
  "style_score": 0.4769,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3242e6ac-bd0d-4ebb-a225-02f9a29bdda0",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.1995,
  "model_score": 0.3212,
  "style_score": 0.2782,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "315768d2-bdf6-415e-bfac-b8272907e78a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.2733,
  "model_score": 0.5727,
  "style_score": 0.125,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "421a1cdc-945a-43ef-a7b4-f942b30c65ed",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5647,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "6038beb2-4b84-4ead-aebf-d8f483829d94",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3089,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "ee6d6594-243c-4221-970c-87f2b8cfcd98",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5353,
  "model_score": 0.7042,
  "style_score": 0.3428,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "20ba93c5-bc78-459e-b383-3e39fc74bde1",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9665,
  "model_score": 0.9792,
  "style_score": 0.6428,
  "label": "Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "af9f6d78-661e-41f3-9ce2-cbb776be093c",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5258,
  "model_score": 0.6175,
  "style_score": 0.4169,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7907ac2e-98dc-43a1-ad74-5623c1b941a4",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6975,
  "model_score": 0.7387,
  "style_score": 0.5246,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "dd57618a-4b2e-4970-bd0d-cb77b07f91d5",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7097,
  "model_score": 0.8051,
  "style_score": 0.4745,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "fe1337ee-d94b-4d51-86de-d1e3c63cc545",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6838,
  "model_score": 0.8329,
  "style_score": 0.4122,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c2de4e52-0981-4e49-b9cc-fae508dab8a2",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7769,
  "model_score": 0.8005,
  "style_score": 0.5687,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "f743b9b3-89f3-4138-bd18-28cc3b0a0738",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6909,
  "model_score": 0.8814,
  "style_score": 0.3732,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "048619ff-156f-4f6e-b7b2-1b8cabc485b2",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7155,
  "model_score": 0.8816,
  "style_score": 0.4057,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "ed5c6b91-cd2a-4313-96e8-f0f5f6f1ab73",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3667,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b6e44dba-9110-48ba-a67e-e151a477c9be",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.2484,
  "model_score": 0.4625,
  "style_score": 0.202,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "14a8bd21-f2a5-47e0-b110-6f29285fb651",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.0505,
  "model_score": 0.2044,
  "style_score": 0.1963,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "63a8d4aa-b9a0-4c86-8e19-7d76cc7e9f3a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4762,
  "model_score": 0.5943,
  "style_score": 0.3739,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "37d42cbf-99d2-45a8-969c-a70b40e949ad",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4026,
  "model_score": 0.4998,
  "style_score": 0.3703,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c4750071-2b03-4f36-9a5b-94730147940c",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4408,
  "model_score": 0.6401,
  "style_score": 0.281,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e7ddc71f-4880-4fd9-8d9a-1c3357621814",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4862,
  "model_score": 0.5583,
  "style_score": 0.4233,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "980a2485-40ca-497e-9200-b643a3c5c6a7",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.125,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "896d89b4-8363-4e45-b637-624b589b88f4",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1334,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "52d79caa-61c2-42b5-adbe-f3c858bcf73a",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8732,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "bf133f9f-3f80-4952-9ab0-ff9b239bd8c8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8727,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "ff23c303-1eeb-483e-a91c-00d2939e1c9c",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.8048,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "8b978897-a2f2-4ab2-8105-58bed9b164c0",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 1.0,
  "model_score": 0.9876,
  "style_score": 0.7827,
  "label": "Our checks suggest this writing may be AI-generated, but we could be wrong. You can appeal if you disagree",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 415,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 415,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "d87d6d25-f334-4a2e-ad14-4cac8f1f0fe0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "1b5866da-c48f-4968-ba2c-429ee83a3bf7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "5d46a10c-15f6-403e-8042-43348f5ac38c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3fe3b712-fc48-4ed0-aaba-0314ec5d7700",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e5e87409-3b2c-4f79-ad51-6bc1098bc636",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "e9434728-8b20-4e80-b78c-7bdc2d5fa9a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "4972aa9b-5d6b-4a18-979b-1e624ef8375a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ba2a09ec-e4ae-4c35-81d9-a078fa67fb86",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "5e4f7680-6a48-46b4-a04e-9851b2ddc50d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d5d30625-c837-4912-9ed3-81f6a05ddcee",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1465,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
