import unittest

from logistics_optimization_lab import LogisticsGraph
from pareto_routes import Route, enumerate_simple_routes, pareto_front


class ParetoRouteTests(unittest.TestCase):
    def test_tradeoff_routes_survive_pareto_filter(self):
        graph = LogisticsGraph()
        graph.add_edge("A", "B", cost=1, time=5, risk=1)
        graph.add_edge("B", "D", cost=1, time=5, risk=1)
        graph.add_edge("A", "C", cost=5, time=1, risk=0.2)
        graph.add_edge("C", "D", cost=5, time=1, risk=0.2)
        front = pareto_front(enumerate_simple_routes(graph, "A", "D"))
        self.assertEqual(len(front), 2)

    def test_dominated_route_removed(self):
        routes = [
            Route(("A", "B"), 1, 1, 1),
            Route(("A", "C"), 2, 2, 2),
        ]
        front = pareto_front(routes)
        self.assertEqual(front, [routes[0]])


if __name__ == "__main__":
    unittest.main()
