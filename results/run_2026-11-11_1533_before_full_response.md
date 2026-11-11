# Run log — before_full_response

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 15:33

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. label coverage |  |   |   |   |  |
| 4. invalid text |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "24e73a98-3ac8-49fb-9fe6-ad86b594c26b",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "9a17a056-9340-4329-9544-810076811c7a",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "9e2a68ea-2259-42ff-b2b3-b0a58780a93f",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "b03bc480-1f3e-4622-af40-1b8bcc4d70de",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "a8eff253-18fb-4b2e-8191-92aa0b2509d8",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.0975,
      "content_id": "6c2a78e8-f373-47bf-ad28-abf031efdacd",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1605,
      "status": "classified",
      "style_score": 0.3028
    },
    "guess": "human",
    "confidence": 0.0975,
    "model_score": 0.1605,
    "style_score": 0.3028,
    "label": "We think this was most likely written by a person.",
    "sent": "In the lyrics the writer uses tone to help the listener to understand "
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6922,
      "content_id": "23746ab7-c5a6-4a9c-a707-d099cf48670e",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6806,
      "status": "classified",
      "style_score": 0.5757
    },
    "guess": "unsure",
    "confidence": 0.6922,
    "model_score": 0.6806,
    "style_score": 0.5757,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "I suppose once you mature, there would be a lot of things that you sai"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5235,
      "content_id": "2a5c409a-55f2-4de3-a3c6-f1c28597aff1",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4512,
      "status": "classified",
      "style_score": 0.5801
    },
    "guess": "unsure",
    "confidence": 0.5235,
    "model_score": 0.4512,
    "style_score": 0.5801,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Now, I understand that those garbage that seems worthless had a lot of"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.7165,
      "content_id": "3d0b25d3-daaa-49dc-bd48-5a6024d5aea9",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7357,
      "status": "classified",
      "style_score": 0.5529
    },
    "guess": "unsure",
    "confidence": 0.7165,
    "model_score": 0.7357,
    "style_score": 0.5529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Not only in high school, I believe that everything I have ever done wa"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3801,
      "content_id": "c7e4049b-d61c-4f7b-9eb1-a77eda229c48",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3359,
      "status": "classified",
      "style_score": 0.5043
    },
    "guess": "unsure",
    "confidence": 0.3801,
    "model_score": 0.3359,
    "style_score": 0.5043,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Classics do not stop influencing readers when they finish reading beca"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "fceb3842-0adc-4176-8899-5d1b532d62f9",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "da5fdc1d-43a7-4147-bf16-9e1263881913",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "b79ec3e6-6599-421b-b977-5320b0ac8a65",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "8e43df87-9d10-401d-8905-7c7f1c845648",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "873239b5-2d50-4b53-9745-6d2cb4cf58cc",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.0975,
      "content_id": "21cbe274-de08-479f-a0ec-9865b72674f9",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1605,
      "status": "classified",
      "style_score": 0.3028
    },
    "guess": "human",
    "confidence": 0.0975,
    "model_score": 0.1605,
    "style_score": 0.3028,
    "label": "We think this was most likely written by a person.",
    "sent": "In the lyrics the writer uses tone to help the listener to understand "
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6922,
      "content_id": "098514f7-3e8c-4066-82ef-78b2195f9f29",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6806,
      "status": "classified",
      "style_score": 0.5757
    },
    "guess": "unsure",
    "confidence": 0.6922,
    "model_score": 0.6806,
    "style_score": 0.5757,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "I suppose once you mature, there would be a lot of things that you sai"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5235,
      "content_id": "9d82d934-c047-4cbb-a34f-c38068ec4cec",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4512,
      "status": "classified",
      "style_score": 0.5801
    },
    "guess": "unsure",
    "confidence": 0.5235,
    "model_score": 0.4512,
    "style_score": 0.5801,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Now, I understand that those garbage that seems worthless had a lot of"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.7165,
      "content_id": "e8b10be7-a336-4ec5-baa9-3173cd250135",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7357,
      "status": "classified",
      "style_score": 0.5529
    },
    "guess": "unsure",
    "confidence": 0.7165,
    "model_score": 0.7357,
    "style_score": 0.5529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Not only in high school, I believe that everything I have ever done wa"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3801,
      "content_id": "84a6c24e-234d-4319-a611-ee462c7b298b",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3359,
      "status": "classified",
      "style_score": 0.5043
    },
    "guess": "unsure",
    "confidence": 0.3801,
    "model_score": 0.3359,
    "style_score": 0.5043,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Classics do not stop influencing readers when they finish reading beca"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "6d77d8a2-fa0e-45d1-b3cd-0fdf9999817c",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "a42e535e-0ecd-4378-9c3a-a88da4223f38",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "8b43f42b-3a6f-482f-b6f4-d47668214f89",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "5b6f0da3-c5f9-4a37-8a0d-ba9abdab8310",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "76633851-7139-4b5d-bda5-1c5f70164ebd",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.0975,
      "content_id": "78e76599-6247-4ba5-a9ac-5fd099bbf8fe",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1605,
      "status": "classified",
      "style_score": 0.3028
    },
    "guess": "human",
    "confidence": 0.0975,
    "model_score": 0.1605,
    "style_score": 0.3028,
    "label": "We think this was most likely written by a person.",
    "sent": "In the lyrics the writer uses tone to help the listener to understand "
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6922,
      "content_id": "bbcd3e98-16e1-4da6-b01c-8b4346994320",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6806,
      "status": "classified",
      "style_score": 0.5757
    },
    "guess": "unsure",
    "confidence": 0.6922,
    "model_score": 0.6806,
    "style_score": 0.5757,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "I suppose once you mature, there would be a lot of things that you sai"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5235,
      "content_id": "f7fce171-83fd-4ec8-b3fe-2366175e13ef",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4512,
      "status": "classified",
      "style_score": 0.5801
    },
    "guess": "unsure",
    "confidence": 0.5235,
    "model_score": 0.4512,
    "style_score": 0.5801,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Now, I understand that those garbage that seems worthless had a lot of"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.7165,
      "content_id": "b6976c92-7128-422a-ad28-f9bb2cb88a00",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7357,
      "status": "classified",
      "style_score": 0.5529
    },
    "guess": "unsure",
    "confidence": 0.7165,
    "model_score": 0.7357,
    "style_score": 0.5529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Not only in high school, I believe that everything I have ever done wa"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3801,
      "content_id": "4218a5d2-b6f7-48a3-82f7-cad8994d97c7",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3359,
      "status": "classified",
      "style_score": 0.5043
    },
    "guess": "unsure",
    "confidence": 0.3801,
    "model_score": 0.3359,
    "style_score": 0.5043,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Classics do not stop influencing readers when they finish reading beca"
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "d23c2115-e37e-4f9e-b048-035b22313da3",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "3620296f-7bce-4e08-bdb2-9e35fe2fc75a",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "ebdaf502-8e86-41c8-83c4-c21b909d847f",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "17afaf96-a01e-403d-a9db-53b69d86bd76",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "b3936918-f7f6-4550-8252-de5fa74439a4",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6417,
      "content_id": "c946441f-1436-4ce3-b967-f351f5f7d86f",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7009,
      "status": "classified",
      "style_score": 0.488
    },
    "guess": "unsure",
    "confidence": 0.6417,
    "model_score": 0.7009,
    "style_score": 0.488,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is a gradual process that requires patience and consistent ef"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6213,
      "content_id": "f93680c6-35ce-4304-a85f-a9f4b108a30b",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6505,
      "status": "classified",
      "style_score": 0.5112
    },
    "guess": "unsure",
    "confidence": 0.6213,
    "model_score": 0.6505,
    "style_score": 0.5112,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service provides benefits for both volunteers and the people"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6059,
      "content_id": "81b1b905-de7d-4676-9359-2c6f1ea291a2",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6522,
      "status": "classified",
      "style_score": 0.489
    },
    "guess": "unsure",
    "confidence": 0.6059,
    "model_score": 0.6522,
    "style_score": 0.489,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Effective teamwork depends on clear communication and shared responsib"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4441,
      "content_id": "7ce670cc-b26a-4bc5-862e-1f1d91e7eaf1",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4496,
      "status": "classified",
      "style_score": 0.4758
    },
    "guess": "unsure",
    "confidence": 0.4441,
    "model_score": 0.4496,
    "style_score": 0.4758,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Literature allows readers to explore experiences beyond their own live"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5149,
      "content_id": "d0ebf095-5c7c-48da-b5d2-5ffffef5b0a6",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5818,
      "status": "classified",
      "style_score": 0.438
    },
    "guess": "unsure",
    "confidence": 0.5149,
    "model_score": 0.5818,
    "style_score": 0.438,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Regular exercise can become easier to maintain when it is part of a co"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5908,
      "content_id": "012788af-2956-40d1-8c7d-c35605c9cb17",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6246,
      "status": "classified",
      "style_score": 0.4965
    },
    "guess": "unsure",
    "confidence": 0.5908,
    "model_score": 0.6246,
    "style_score": 0.4965,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is an essential life skill; it requires time and sacrifice.\nS"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3596,
      "content_id": "ac2767a3-b869-47a3-9574-e6e140584a00",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5599,
      "status": "classified",
      "style_score": 0.2529
    },
    "guess": "unsure",
    "confidence": 0.3596,
    "model_score": 0.5599,
    "style_score": 0.2529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service can be beneficial not only to the community but to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4516,
      "content_id": "058ce97b-bab9-4a5e-b669-ded08336266c",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4906,
      "status": "classified",
      "style_score": 0.4449
    },
    "guess": "unsure",
    "confidence": 0.4516,
    "model_score": 0.4906,
    "style_score": 0.4449,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Teamwork can be hard with the mind of a narcissist as they want to hel"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.2151,
      "content_id": "18a1ea37-0474-400c-b4cc-97afbb525dad",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3456,
      "status": "classified",
      "style_score": 0.2745
    },
    "guess": "unsure",
    "confidence": 0.2151,
    "model_score": 0.3456,
    "style_score": 0.2745,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "creativity and Imagination are key in a child's life, and one way to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4015,
      "content_id": "0ebda84f-9232-45c7-9a7d-ffdee433643d",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4738,
      "status": "classified",
      "style_score": 0.3949
    },
    "guess": "unsure",
    "confidence": 0.4015,
    "model_score": 0.4738,
    "style_score": 0.3949,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Exercise is a part of discipline too; a healthy mind needs a healthy b"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "8bd033b0-7bb7-4fd9-91c7-dcbc490a96d9",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "92c29e0e-4adb-4375-aad4-21d7e3efd90a",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "e6762641-cdb1-46a0-9943-43d9211683c6",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "6a2ed206-c866-4549-9cee-7c8a458f4196",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "5d85de5b-3a33-4fb1-92a7-50f92336c141",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6417,
      "content_id": "8b5ec4c1-2ec7-4c0d-8aea-6ecbeb327461",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7009,
      "status": "classified",
      "style_score": 0.488
    },
    "guess": "unsure",
    "confidence": 0.6417,
    "model_score": 0.7009,
    "style_score": 0.488,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is a gradual process that requires patience and consistent ef"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6213,
      "content_id": "1b3ab5f0-fa49-4476-ac2d-8ea28c719d99",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6505,
      "status": "classified",
      "style_score": 0.5112
    },
    "guess": "unsure",
    "confidence": 0.6213,
    "model_score": 0.6505,
    "style_score": 0.5112,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service provides benefits for both volunteers and the people"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6059,
      "content_id": "4b2a4aa0-273c-4629-b6e6-1bd45a60483d",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6522,
      "status": "classified",
      "style_score": 0.489
    },
    "guess": "unsure",
    "confidence": 0.6059,
    "model_score": 0.6522,
    "style_score": 0.489,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Effective teamwork depends on clear communication and shared responsib"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4441,
      "content_id": "1900b153-a767-4cb5-9068-75580f9c00bf",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4496,
      "status": "classified",
      "style_score": 0.4758
    },
    "guess": "unsure",
    "confidence": 0.4441,
    "model_score": 0.4496,
    "style_score": 0.4758,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Literature allows readers to explore experiences beyond their own live"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5149,
      "content_id": "8bb49146-f712-441a-a8b7-ea92e0885c03",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5818,
      "status": "classified",
      "style_score": 0.438
    },
    "guess": "unsure",
    "confidence": 0.5149,
    "model_score": 0.5818,
    "style_score": 0.438,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Regular exercise can become easier to maintain when it is part of a co"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5908,
      "content_id": "d7302284-3ff9-46a4-9ea3-0a75c86e5220",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6246,
      "status": "classified",
      "style_score": 0.4965
    },
    "guess": "unsure",
    "confidence": 0.5908,
    "model_score": 0.6246,
    "style_score": 0.4965,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is an essential life skill; it requires time and sacrifice.\nS"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3596,
      "content_id": "d53a2deb-595e-4c77-95a6-4acc05bde855",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5599,
      "status": "classified",
      "style_score": 0.2529
    },
    "guess": "unsure",
    "confidence": 0.3596,
    "model_score": 0.5599,
    "style_score": 0.2529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service can be beneficial not only to the community but to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4516,
      "content_id": "d079a5fc-2db3-4bed-b3dc-94644fa7a26d",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4906,
      "status": "classified",
      "style_score": 0.4449
    },
    "guess": "unsure",
    "confidence": 0.4516,
    "model_score": 0.4906,
    "style_score": 0.4449,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Teamwork can be hard with the mind of a narcissist as they want to hel"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.2151,
      "content_id": "e1dddfcc-c54e-4a3d-a52a-6777c91b7b02",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3456,
      "status": "classified",
      "style_score": 0.2745
    },
    "guess": "unsure",
    "confidence": 0.2151,
    "model_score": 0.3456,
    "style_score": 0.2745,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "creativity and Imagination are key in a child's life, and one way to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4015,
      "content_id": "cb27167c-58f4-45f0-b709-cbe53e8bff18",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4738,
      "status": "classified",
      "style_score": 0.3949
    },
    "guess": "unsure",
    "confidence": 0.4015,
    "model_score": 0.4738,
    "style_score": 0.3949,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Exercise is a part of discipline too; a healthy mind needs a healthy b"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "response": {
      "confidence": 0.3167,
      "content_id": "b15604e0-106c-45d7-b4d8-ac517204b49e",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.2209,
      "status": "classified",
      "style_score": 0.5347
    },
    "guess": "unsure",
    "confidence": 0.3167,
    "model_score": 0.2209,
    "style_score": 0.5347,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In International news, being the number one problem in Ukraine\u2019s corru"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5667,
      "content_id": "6f992fda-b94d-4c4b-b508-3333d9d44e41",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.619,
      "status": "classified",
      "style_score": 0.47
    },
    "guess": "unsure",
    "confidence": 0.5667,
    "model_score": 0.619,
    "style_score": 0.47,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "The founding mothers of the United States Feminist movement understood"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5977,
      "content_id": "a132b83f-09fe-4c52-ad25-51a3cf3af7e0",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6303,
      "status": "classified",
      "style_score": 0.5
    },
    "guess": "unsure",
    "confidence": 0.5977,
    "model_score": 0.6303,
    "style_score": 0.5,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Every Saturday, the Al-Hikmah mosque also offers Saturday School, wher"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.1164,
      "content_id": "a78aa710-a93e-4b76-98e5-1ee8de50a162",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.1998,
      "status": "classified",
      "style_score": 0.2887
    },
    "guess": "human",
    "confidence": 0.1164,
    "model_score": 0.1998,
    "style_score": 0.2887,
    "label": "We think this was most likely written by a person.",
    "sent": "In the prologue from Romeo and Juliet  buy william shakespeare the aut"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5064,
      "content_id": "af121715-3b43-40fc-b94d-facc4e0945a8",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4644,
      "status": "classified",
      "style_score": 0.5441
    },
    "guess": "unsure",
    "confidence": 0.5064,
    "model_score": 0.4644,
    "style_score": 0.5441,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "In the song who knows from west side story by stephen sondheim  uses r"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6417,
      "content_id": "787f80fb-fdbe-4f2f-b1ac-c37aac8b2e99",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.7009,
      "status": "classified",
      "style_score": 0.488
    },
    "guess": "unsure",
    "confidence": 0.6417,
    "model_score": 0.7009,
    "style_score": 0.488,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is a gradual process that requires patience and consistent ef"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6213,
      "content_id": "40c6e773-e57b-49e1-aeeb-c2d3284a4d04",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6505,
      "status": "classified",
      "style_score": 0.5112
    },
    "guess": "unsure",
    "confidence": 0.6213,
    "model_score": 0.6505,
    "style_score": 0.5112,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service provides benefits for both volunteers and the people"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.6059,
      "content_id": "a214bf9a-3561-4ab3-a09c-e825960989e4",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6522,
      "status": "classified",
      "style_score": 0.489
    },
    "guess": "unsure",
    "confidence": 0.6059,
    "model_score": 0.6522,
    "style_score": 0.489,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Effective teamwork depends on clear communication and shared responsib"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4441,
      "content_id": "3f2492bc-508f-44ff-be66-91cdc7144fec",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4496,
      "status": "classified",
      "style_score": 0.4758
    },
    "guess": "unsure",
    "confidence": 0.4441,
    "model_score": 0.4496,
    "style_score": 0.4758,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Literature allows readers to explore experiences beyond their own live"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5149,
      "content_id": "24c33a75-f95a-4621-a460-33af3ba34cd2",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5818,
      "status": "classified",
      "style_score": 0.438
    },
    "guess": "unsure",
    "confidence": 0.5149,
    "model_score": 0.5818,
    "style_score": 0.438,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Regular exercise can become easier to maintain when it is part of a co"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.5908,
      "content_id": "6ab41c6d-12b5-46f1-89a8-d795b00001af",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.6246,
      "status": "classified",
      "style_score": 0.4965
    },
    "guess": "unsure",
    "confidence": 0.5908,
    "model_score": 0.6246,
    "style_score": 0.4965,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Learning is an essential life skill; it requires time and sacrifice.\nS"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.3596,
      "content_id": "e490e04a-a865-4eef-948a-d9649cfe400e",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.5599,
      "status": "classified",
      "style_score": 0.2529
    },
    "guess": "unsure",
    "confidence": 0.3596,
    "model_score": 0.5599,
    "style_score": 0.2529,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Community service can be beneficial not only to the community but to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4516,
      "content_id": "5b07fa8b-25ff-4c6f-b230-244c67754f34",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4906,
      "status": "classified",
      "style_score": 0.4449
    },
    "guess": "unsure",
    "confidence": 0.4516,
    "model_score": 0.4906,
    "style_score": 0.4449,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Teamwork can be hard with the mind of a narcissist as they want to hel"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.2151,
      "content_id": "532afc0a-7c76-41f0-9883-e140da6cf75c",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.3456,
      "status": "classified",
      "style_score": 0.2745
    },
    "guess": "unsure",
    "confidence": 0.2151,
    "model_score": 0.3456,
    "style_score": 0.2745,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "creativity and Imagination are key in a child's life, and one way to t"
  },
  {
    "status": 200,
    "response": {
      "confidence": 0.4015,
      "content_id": "3e313e8b-e781-497a-8bc5-6b6e285a65de",
      "guess": "unsure",
      "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
      "model_score": 0.4738,
      "status": "classified",
      "style_score": 0.3949
    },
    "guess": "unsure",
    "confidence": 0.4015,
    "model_score": 0.4738,
    "style_score": 0.3949,
    "label": "We couldn\u2019t tell whether a person or AI wrote this. It could be either.",
    "sent": "Exercise is a part of discipline too; a healthy mind needs a healthy b"
  }
]
```

### invalid text

**Trial 1**

```json
[
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " "
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_number\"}"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " "
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_number\"}"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " "
  },
  {
    "status": 400,
    "response": {
      "error": "text must be a nonempty string."
    },
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_number\"}"
  }
]
```
