import unittest

from logistics_optimization_lab import LogisticsGraph


class LogisticsOptimizationTests(unittest.TestCase):
    def test_selects_lower_weighted_route(self):
        g = LogisticsGraph()
        g.add_edge("A", "C", cost=10, time=1, risk=0)
        g.add_edge("A", "B", cost=2, time=2, risk=0)
        g.add_edge("B", "C", cost=2, time=2, risk=0)
        self.assertEqual(g.route("A", "C", cost_weight=1, time_weight=0)["path"], ["A", "B", "C"])

    def test_time_weight_changes_choice(self):
        g = LogisticsGraph()
        g.add_edge("A", "C", cost=10, time=1)
        g.add_edge("A", "B", cost=1, time=5)
        g.add_edge("B", "C", cost=1, time=5)
        self.assertEqual(g.route("A", "C", cost_weight=0, time_weight=1)["path"], ["A", "C"])

    def test_no_route_raises(self):
        g = LogisticsGraph()
        with self.assertRaises(ValueError):
            g.route("A", "B")

    def test_blocked_edges_are_excluded(self):
        g = LogisticsGraph()
        g.add_edge("A", "C", cost=1, time=1, blocked=True)
        g.add_edge("A", "B", cost=2, time=2)
        g.add_edge("B", "C", cost=2, time=2)
        self.assertEqual(g.route("A", "C")["path"], ["A", "B", "C"])

    def test_negative_or_non_finite_edge_values_are_rejected(self):
        g = LogisticsGraph()
        for value in (-1, float("nan"), float("inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    g.add_edge("A", "B", cost=value, time=1)

    def test_negative_or_non_finite_objective_weights_are_rejected(self):
        g = LogisticsGraph()
        g.add_edge("A", "B", cost=1, time=1)
        for value in (-1, float("nan"), float("inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    g.route("A", "B", risk_weight=value)

    def test_start_equals_goal_returns_zero_cost_route(self):
        self.assertEqual(
            LogisticsGraph().route("A", "A"),
            {"path": ["A"], "objective": 0.0, "cost": 0.0, "time": 0.0, "risk": 0.0},
        )


if __name__ == "__main__":
    unittest.main()
