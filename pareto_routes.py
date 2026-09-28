from __future__ import annotations

from dataclasses import dataclass

from logistics_optimization_lab import LogisticsGraph


@dataclass(frozen=True)
class Route:
    path: tuple[str, ...]
    cost: float
    time: float
    risk: float


def enumerate_simple_routes(
    graph: LogisticsGraph,
    start: str,
    goal: str,
    *,
    max_hops: int = 6,
) -> list[Route]:
    if max_hops < 1:
        raise ValueError("max_hops must be >= 1")

    routes: list[Route] = []

    def visit(node: str, path: list[str], cost: float, time: float, risk: float) -> None:
        if len(path) - 1 > max_hops:
            return
        if node == goal:
            routes.append(Route(tuple(path), cost, time, risk))
            return

        for edge in graph.adj.get(node, []):
            if edge.blocked or edge.to in path:
                continue
            visit(
                edge.to,
                path + [edge.to],
                cost + edge.cost,
                time + edge.time,
                risk + edge.risk,
            )

    visit(start, [start], 0.0, 0.0, 0.0)
    return routes


def dominates(a: Route, b: Route) -> bool:
    no_worse = a.cost <= b.cost and a.time <= b.time and a.risk <= b.risk
    strictly_better = a.cost < b.cost or a.time < b.time or a.risk < b.risk
    return no_worse and strictly_better


def pareto_front(routes: list[Route]) -> list[Route]:
    return [
        route
        for route in routes
        if not any(dominates(other, route) for other in routes if other != route)
    ]


if __name__ == "__main__":
    graph = LogisticsGraph()
    graph.add_edge("A", "B", cost=2, time=5, risk=1)
    graph.add_edge("B", "D", cost=2, time=5, risk=1)
    graph.add_edge("A", "C", cost=6, time=2, risk=0.2)
    graph.add_edge("C", "D", cost=6, time=2, risk=0.2)
    print(pareto_front(enumerate_simple_routes(graph, "A", "D")))
