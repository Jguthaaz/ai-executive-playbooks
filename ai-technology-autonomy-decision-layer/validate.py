"""Documentation and synthetic arithmetic checks; no model/client evaluation."""
import json
import math
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = json.loads((HERE / "case-scorecard.json").read_text(encoding="utf-8"))
CRITERIA = ["task_fit", "simplicity", "cost", "capability", "control", "time"]
GATES = {"data", "authority", "quality", "budget", "evaluation"}


def numeric(value):
    return type(value) in (int, float) and math.isfinite(value)


def total(weights, scores):
    if len(weights) != 6 or any(not numeric(w) or w < 0 for w in weights):
        raise ValueError("Six finite nonnegative weights required")
    if not math.isclose(sum(weights), 100):
        raise ValueError("Weights must sum to 100")
    if len(scores) != 6:
        raise ValueError("Six scores required")
    if any(s is not None and (not numeric(s) or not 1 <= s <= 5) for s in scores):
        raise ValueError("Scores must be unknown or finite values from 1 to 5")
    if None in scores:
        return None
    return sum(w * s for w, s in zip(weights, scores)) / 100


def eligible(gates):
    if set(gates) != GATES:
        raise ValueError("Complete gate register required")
    if any(v not in ("pass", "fail", "unknown") for v in gates.values()):
        raise ValueError("Invalid gate status")
    return all(v == "pass" for v in gates.values())


class DecisionChecks(unittest.TestCase):
    def test_default_totals(self):
        self.assertEqual(DATA["criteria"], CRITERIA)
        for option in DATA["options"]:
            self.assertAlmostEqual(total(DATA["weights"], option["scores"]),
                                   option["expected_total"])

    def test_sensitivity(self):
        for scenario in DATA["scenarios"]:
            values = [
                total(scenario["weights"], scenario.get("overrides", {}).get(o["id"], o["scores"]))
                for o in DATA["options"]
            ]
            for actual, expected in zip(values, scenario["expected_totals"]):
                self.assertAlmostEqual(actual, expected)
            leader = DATA["options"][values.index(max(values))]["id"]
            self.assertEqual(leader, scenario["expected_leader"])

    def test_cost_subtotals(self):
        costs = DATA['cost_estimates']
        for option in costs['options']:
            self.assertEqual(option['setup'] + costs['months'] * option['monthly'] + option['exit'],
                             option['expected_subtotal'])

    def test_tie_boundary(self):
        weights = [37.5] + [12.5] * 5
        self.assertAlmostEqual(total(weights, DATA["options"][0]["scores"]),
                               total(weights, DATA["options"][1]["scores"]))

    def test_missing_scores_stay_unknown(self):
        self.assertIsNone(total(DATA["weights"], [None, 5, 5, 5, 5, 5]))

    def test_invalid_inputs(self):
        for weights, scores in [
            ([20] * 6, [5] * 6), ([-1, 21, 20, 20, 20, 20], [5] * 6),
            ([100], [5] * 6), (DATA["weights"], [6] * 6),
            (DATA["weights"], [0] * 6), (DATA["weights"], [True] * 6),
            (DATA["weights"], [float("nan")] * 6),
            ([float("inf")] * 6, [5] * 6), (DATA["weights"], [5] * 5),
        ]:
            with self.subTest(weights=weights, scores=scores):
                with self.assertRaises(ValueError):
                    total(weights, scores)

    def test_gates_override_scores(self):
        passed = dict.fromkeys(GATES, "pass")
        self.assertTrue(eligible(passed))
        for gate in GATES:
            for status in ("unknown", "fail"):
                self.assertFalse(eligible({**passed, gate: status}))
        self.assertEqual(total(DATA["weights"], [5] * 6), 5)
        self.assertTrue(all(not eligible(o["gates"]) for o in DATA["options"]))
        self.assertEqual(DATA["options"][2]["gates"]["authority"], "fail")
        with self.assertRaises(ValueError):
            eligible({"data": "pass"})
        with self.assertRaises(ValueError):
            eligible({**passed, "data": "approved"})

    def test_document_links(self):
        docs = list(HERE.glob("*.md")) + [
            ROOT / "README.md", ROOT / "PORTFOLIO-GUIDE.md",
            ROOT / "ROADMAP.md", ROOT / "examples/quotation-assistant.md",
        ]
        checked = 0
        for doc in docs:
            for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                path = unquote(target.split("#", 1)[0])
                with self.subTest(doc=doc.name, link=target):
                    self.assertTrue((doc.parent / path).exists(), target)
                checked += 1
        self.assertGreater(checked, 50)

    def test_attribution_and_artifacts(self):
        for name in ("technology-decision-canvas.md", "solution-selection-tree.md",
                     "architecture-trade-off-scorecard.md", "executive-decision-brief.md"):
            self.assertTrue((HERE / name).is_file())
        notice = (HERE / "third-party/Microsoft-AI-Decision-Framework-LICENSE.txt").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) Microsoft Corporation.", notice)
        self.assertIn('THE SOFTWARE IS PROVIDED "AS IS"', notice)


if __name__ == "__main__":
    unittest.main(verbosity=2)
