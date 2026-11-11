import json
import uuid
from datetime import datetime
from pathlib import Path

import requests
from scenarios import SCENARIOS


BASE_URL = "http://127.0.0.1:5000"


def call(method, route, body=None):
    response = requests.request(
        method,
        BASE_URL + route,
        json=body,
        timeout=90,
    )
    try:
        payload = response.json()
    except ValueError:
        payload = {"non_json_response": response.text}

    return {
        "http_status": response.status_code,
        "response": payload,
    }


def get_history(content_id):
    result = call("GET", "/log")
    if result["http_status"] != 200:
        raise RuntimeError(f"Could not read audit log: {result}")

    entries = result["response"]["entries"]
    return [
        entry for entry in entries
        if entry.get("content_id") == content_id
    ]


def main():
    human_scenario = next(
        s for s in SCENARIOS if s["criterion"] == 1
    )
    texts = human_scenario["texts"][:5]
    if len(texts) != 5:
        raise ValueError("This test requires five writing samples.")

    run_id = uuid.uuid4().hex[:12]
    trials = []

    for trial in range(1, 4):
        results = []

        for number, text in enumerate(texts, 1):
            creator = f"appeal_eval_{run_id}_{number}"
            reasoning = (
                f"I wrote sample {number} myself. "
                "Please review the classification."
            )
            row = {
                "sample": number,
                "creator_id": creator,
                "reasoning": reasoning,
                "passed": False,
            }

            try:
                submission = call(
                    "POST",
                    "/submit",
                    {"text": text, "creator_id": creator},
                )
                row["submission"] = submission

                if submission["http_status"] != 200:
                    raise RuntimeError("Submission did not return 200.")

                content_id = submission["response"]["content_id"]
                before = get_history(content_id)
                row["history_before"] = before

                original = next(
                    entry for entry in before
                    if "event" not in entry
                )

                appeal = call(
                    "POST",
                    "/appeal",
                    {
                        "content_id": content_id,
                        "reasoning": reasoning,
                    },
                )
                row["appeal"] = appeal

                after = get_history(content_id)
                row["history_after"] = after

                payload = appeal["response"]
                appeal_entries = [
                    entry for entry in after
                    if entry.get("event") == "appeal"
                ]
                matching_appeals = [
                    entry for entry in appeal_entries
                    if entry.get("content_id") == content_id
                    and entry.get("creator_id") == creator
                    and entry.get("reasoning") == reasoning
                    and entry.get("status") == "under_review"
                ]

                checks = {
                    "appeal_returns_200":
                        appeal["http_status"] == 200,

                    "correct_content_id":
                        payload.get("content_id") == content_id,

                    "response_status_under_review":
                        payload.get("status") == "under_review",

                    "nonempty_confirmation":
                        isinstance(payload.get("message"), str)
                        and bool(payload["message"].strip()),

                    "original_decision_preserved":
                        original in after,

                    "exact_reasoning_and_ids_logged":
                        len(matching_appeals) == 1,

                    "one_new_appeal_record":
                        len(after) == len(before) + 1
                        and len(appeal_entries) == 1,

                    "latest_record_under_review":
                        bool(after)
                        and after[-1].get("event") == "appeal"
                        and after[-1].get("status") == "under_review",
                }

                row["checks"] = checks
                row["passed"] = all(checks.values())

            except Exception as exc:
                row["error"] = f"{type(exc).__name__}: {exc}"

            results.append(row)

        passed = sum(row["passed"] for row in results)
        print(f"Trial {trial}: {passed}/5 appeals passed")
        trials.append({
            "trial": trial,
            "passed": passed,
            "results": results,
        })

    report = {
        "criterion": 3,
        "phase": "after",
        "produced_by": "test_appeals.py::main",
        "target": "All five appeals pass every check in every trial",
        "status_check": (
            "Current status is read from the latest audit entry "
            "for the submission; the original decision stays unchanged."
        ),
        "trials": trials,
        "verdict": (
            "MET" if all(t["passed"] == 5 for t in trials)
            else "MISSED"
        ),
    }

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    folder = Path(__file__).resolve().parent / "results"
    folder.mkdir(exist_ok=True)
    path = folder / f"appeals_{stamp}_after.json"
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True),
        encoding="utf-8",
    )

    print("Verdict:", report["verdict"])
    print("Saved:", path)


if __name__ == "__main__":
    main()