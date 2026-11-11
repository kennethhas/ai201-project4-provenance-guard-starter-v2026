# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 15:51
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `0aec7dae-638e-4fe8-a1fc-52e54d76b479` | unsure | 0.236 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `08cc4169-5056-4541-b4bd-2104ce145b6b` | unsure | 0.318 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0229c05d-9021-4764-8fdd-df33e3c88a6c` | unsure | 0.518 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `60afbbdb-7361-4962-8007-3ce449182f61` | unsure | 0.566 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `5fd2e59b-85cf-420f-9159-bce0f8aa4543` | unsure | 0.200 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `07382bbb-70fe-42b6-90ba-4c0361d6b1f4` | unsure | 0.273 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ad5b385b-6962-49f1-b4ef-8be21653b82c` | unsure | 0.565 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `25eded8f-3920-4dd6-903f-c3c4c1285558` | unsure | 0.309 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c3be15fe-fd1b-4dcf-a505-0c1acfb96de6` | unsure | 0.535 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `beb81766-59cf-4eaf-8602-e892816016c9` | ai | 0.967 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `87bed70c-dd49-409f-9375-b2c4f70ccf2a` | unsure | 0.526 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e0622754-2b76-4296-8912-d000beba45e1` | unsure | 0.698 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `0ed209fa-04d8-4e9b-9ab1-aef1e31c79ff` | unsure | 0.710 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `643bf14b-29e1-4bc6-9dbe-d1a26cbb5b29` | unsure | 0.684 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `0087ff2e-2cd1-4e00-999f-15a4b430e18c` | unsure | 0.777 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b57a81af-7dff-452a-ae2b-b8bf3c7242ed` | unsure | 0.691 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `40311693-e015-4e59-b59a-eb851796fa2e` | unsure | 0.716 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `14aea1b4-20dc-4e1f-89a9-41568ce71c81` | unsure | 0.367 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `2f9b754b-e576-4d43-a681-680cd81b9511` | unsure | 0.248 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0ed7ddf1-d6a8-4816-b2f0-3e0071cba797` | human | 0.051 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f8b265bd-5052-4725-a80b-024f2ad5959f` | unsure | 0.476 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ab5999a3-73b0-4c1d-b567-ce3cfe61082f` | unsure | 0.403 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `454cb250-db39-43ce-beff-19413ea26aa7` | unsure | 0.441 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6fe6ba4a-8648-41c7-b767-00294ccd1ce2` | unsure | 0.486 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `7fafeaa5-7d1c-463d-a8f8-49fab9d6f3a7` | human | 0.125 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 200 | `346b1c4c-f32f-4c73-ab45-ba5f381f2c59` | ai | 0.873 |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `5d8ad36f-26fd-40fc-a815-fd6939bac57a` | unsure | 0.805 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `53e1f2e1-2ca9-4bb4-a434-3f26d82ea869` | ai | 1.000 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `22af87fb-3de6-4d6e-9889-f63599f9c623` | human | 0.146 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fb78a88e-0879-403f-b0be-1446d1000fa2` | human | 0.146 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5eed5009-8d6b-468b-9de4-9b35906475ca` | human | 0.146 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dc61c93-0e10-49f1-9356-b032886380c0` | human | 0.146 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f24e92f7-e8f7-441b-a2d4-95b0ae2f28e3` | human | 0.146 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `659a07ad-504e-49b3-8243-0652dd6ce2c5` | human | 0.146 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e132cf9b-e151-4d96-b2d6-7e236d95f583` | human | 0.146 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `781730a9-4bf8-4d2a-aba7-34c495a04800` | human | 0.146 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6d21600f-a35e-4589-a952-a6654b17140f` | human | 0.146 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `97f64f8f-a191-4ae0-b604-a26c38c25c56` | human | 0.146 |  |
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
  "content_id": "0aec7dae-638e-4fe8-a1fc-52e54d76b479",
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
  "content_id": "08cc4169-5056-4541-b4bd-2104ce145b6b",
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
  "content_id": "0229c05d-9021-4764-8fdd-df33e3c88a6c",
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
  "content_id": "60afbbdb-7361-4962-8007-3ce449182f61",
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
  "content_id": "5fd2e59b-85cf-420f-9159-bce0f8aa4543",
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
  "content_id": "07382bbb-70fe-42b6-90ba-4c0361d6b1f4",
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
  "content_id": "ad5b385b-6962-49f1-b4ef-8be21653b82c",
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
  "content_id": "25eded8f-3920-4dd6-903f-c3c4c1285558",
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
  "content_id": "c3be15fe-fd1b-4dcf-a505-0c1acfb96de6",
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
  "content_id": "beb81766-59cf-4eaf-8602-e892816016c9",
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
  "content_id": "87bed70c-dd49-409f-9375-b2c4f70ccf2a",
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
  "content_id": "e0622754-2b76-4296-8912-d000beba45e1",
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
  "content_id": "0ed209fa-04d8-4e9b-9ab1-aef1e31c79ff",
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
  "content_id": "643bf14b-29e1-4bc6-9dbe-d1a26cbb5b29",
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
  "content_id": "0087ff2e-2cd1-4e00-999f-15a4b430e18c",
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
  "content_id": "b57a81af-7dff-452a-ae2b-b8bf3c7242ed",
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
  "content_id": "40311693-e015-4e59-b59a-eb851796fa2e",
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
  "content_id": "14aea1b4-20dc-4e1f-89a9-41568ce71c81",
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
  "content_id": "2f9b754b-e576-4d43-a681-680cd81b9511",
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
  "content_id": "0ed7ddf1-d6a8-4816-b2f0-3e0071cba797",
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
  "content_id": "f8b265bd-5052-4725-a80b-024f2ad5959f",
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
  "content_id": "ab5999a3-73b0-4c1d-b567-ce3cfe61082f",
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
  "content_id": "454cb250-db39-43ce-beff-19413ea26aa7",
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
  "content_id": "6fe6ba4a-8648-41c7-b767-00294ccd1ce2",
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
  "content_id": "7fafeaa5-7d1c-463d-a8f8-49fab9d6f3a7",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "346b1c4c-f32f-4c73-ab45-ba5f381f2c59",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "5d8ad36f-26fd-40fc-a815-fd6939bac57a",
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
  "content_id": "53e1f2e1-2ca9-4bb4-a434-3f26d82ea869",
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
  "content_id": "22af87fb-3de6-4d6e-9889-f63599f9c623",
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
  "content_id": "fb78a88e-0879-403f-b0be-1446d1000fa2",
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
  "content_id": "5eed5009-8d6b-468b-9de4-9b35906475ca",
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
  "content_id": "6dc61c93-0e10-49f1-9356-b032886380c0",
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
  "content_id": "f24e92f7-e8f7-441b-a2d4-95b0ae2f28e3",
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
  "content_id": "659a07ad-504e-49b3-8243-0652dd6ce2c5",
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
  "content_id": "e132cf9b-e151-4d96-b2d6-7e236d95f583",
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
  "content_id": "781730a9-4bf8-4d2a-aba7-34c495a04800",
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
  "content_id": "6d21600f-a35e-4589-a952-a6654b17140f",
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
  "content_id": "97f64f8f-a191-4ae0-b604-a26c38c25c56",
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
