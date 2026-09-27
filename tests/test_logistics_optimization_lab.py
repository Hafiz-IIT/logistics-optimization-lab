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


if __name__ == "__main__":
    unittest.main()
