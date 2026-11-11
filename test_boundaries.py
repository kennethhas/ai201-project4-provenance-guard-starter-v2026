import json
from datetime import datetime
from pathlib import Path

from scoring import score_to_label


cases = [
    (0.00, "human"),
    (0.14, "human"),
    (0.15, "human"),
    (0.16, "unsure"),
    (0.50, "unsure"),
    (0.84, "unsure"),
    (0.85, "ai"),
    (0.86, "ai"),
    (1.00, "ai"),
]

expected_labels = {
    "human": "We think this was most likely written by a person.",
    "unsure": (
        "We couldn\u2019t tell whether a person or AI wrote this. "
        "It could be either."
    ),
    "ai": (
        "Our checks suggest this writing may be AI-generated, "
        "but we could be wrong. You can appeal if you disagree"
    ),
}


def main():
    trials = []

    for trial in range(1, 4):
        results = []

        for score, expected_guess in cases:
            row = {
                "score": score,
                "expected_guess": expected_guess,
                "expected_label": expected_labels[expected_guess],
            }

            try:
                guess, label = score_to_label(score)
                row.update({
                    "actual_guess": guess,
                    "actual_label": label,
                    "passed": (
                        guess == expected_guess
                        and label == expected_labels[expected_guess]
                    ),
                })
            except Exception as exc:
                row.update({
                    "passed": False,
                    "error": f"{type(exc).__name__}: {exc}",
                })

            results.append(row)

        passed = sum(row["passed"] for row in results)
        print(f"Trial {trial}: {passed}/9 matched")
        trials.append({
            "trial": trial,
            "passed": passed,
            "results": results,
        })

    report = {
        "criterion": 5,
        "phase": "after",
        "produced_by": "test_boundaries.py::main",
        "tested_function": "scoring.py::score_to_label",
        "target": "9/9 correct categories and exact labels in every trial",
        "trials": trials,
        "verdict": (
            "MET" if all(t["passed"] == 9 for t in trials)
            else "MISSED"
        ),
    }

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    folder = Path(__file__).resolve().parent / "results"
    folder.mkdir(exist_ok=True)
    path = folder / f"boundaries_{stamp}_after.json"

    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True),
        encoding="utf-8",
    )

    print("Verdict:", report["verdict"])
    print("Saved:", path)


if __name__ == "__main__":
    main()