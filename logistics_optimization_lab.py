from __future__ import annotations

from dataclasses import dataclass
import heapq
from math import inf, isfinite


@dataclass(frozen=True)
class Edge:
    to: str
    cost: float
    time: float
    risk: float = 0.0
    blocked: bool = False


class LogisticsGraph:
    def __init__(self):
        self.adj: dict[str, list[Edge]] = {}

    @staticmethod
    def _validate_nonnegative(name: str, value: float) -> float:
        try:
            number = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"{name} must be a finite non-negative number") from None
        if not isfinite(number) or number < 0:
            raise ValueError(f"{name} must be finite and non-negative")
        return number

    def add_edge(self, a: str, b: str, *, cost: float, time: float, risk: float = 0.0,
                 bidirectional: bool = True, blocked: bool = False) -> None:
        if not isinstance(a, str) or not a.strip() or not isinstance(b, str) or not b.strip():
            raise ValueError("edge endpoints must be non-empty strings")
        cost = self._validate_nonnegative("cost", cost)
        time = self._validate_nonnegative("time", time)
        risk = self._validate_nonnegative("risk", risk)
        self.adj.setdefault(a, []).append(Edge(b, cost, time, risk, blocked))
        if bidirectional:
            self.adj.setdefault(b, []).append(Edge(a, cost, time, risk, blocked))

    def route(self, start: str, goal: str, *, cost_weight: float = 1.0, time_weight: float = 1.0, risk_weight: float = 1.0):
        if not isinstance(start, str) or not start.strip() or not isinstance(goal, str) or not goal.strip():
            raise ValueError("start and goal must be non-empty strings")
        weights = (cost_weight, time_weight, risk_weight)
        weights = tuple(
            self._validate_nonnegative(name, weight)
            for name, weight in zip(("cost_weight", "time_weight", "risk_weight"), weights)
        )
        q = [(0.0, start)]
        dist = {start: 0.0}
        prev: dict[str, tuple[str, Edge]] = {}

        while q:
            score, node = heapq.heappop(q)
            if score != dist.get(node):
                continue
            if node == goal:
                break
            for edge in self.adj.get(node, []):
                if edge.blocked:
                    continue
                edge_score = weights[0] * edge.cost + weights[1] * edge.time + weights[2] * edge.risk
                new = score + edge_score
                if new < dist.get(edge.to, inf):
                    dist[edge.to] = new
                    prev[edge.to] = (node, edge)
                    heapq.heappush(q, (new, edge.to))

        if goal not in dist:
            raise ValueError("no route")

        path = [goal]
        totals = {"cost": 0.0, "time": 0.0, "risk": 0.0}
        cur = goal
        while cur != start:
            parent, edge = prev[cur]
            totals["cost"] += edge.cost
            totals["time"] += edge.time
            totals["risk"] += edge.risk
            path.append(parent)
            cur = parent
        path.reverse()
        return {"path": path, "objective": dist[goal], **totals}


if __name__ == "__main__":
    g = LogisticsGraph()
    g.add_edge("warehouse", "port", cost=5, time=2, risk=1)
    g.add_edge("warehouse", "hub", cost=2, time=1, risk=0.2)
    g.add_edge("hub", "port", cost=2, time=1, risk=0.2)
    print(g.route("warehouse", "port"))
