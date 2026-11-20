from __future__ import annotations

from dataclasses import dataclass
import heapq
from math import inf, isfinite


def _finite_nonnegative(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or value < 0:
        raise ValueError(f"{name} must be a finite non-negative number")
    return float(value)


@dataclass(frozen=True)
class Edge:
    to: str
    cost: float
    time: float
    risk: float = 0.0
    blocked: bool = False

    def __post_init__(self):
        if not isinstance(self.to, str) or not self.to.strip():
            raise ValueError("destination must be a non-empty string")
        _finite_nonnegative("cost", self.cost)
        _finite_nonnegative("time", self.time)
        _finite_nonnegative("risk", self.risk)
        if not isinstance(self.blocked, bool):
            raise ValueError("blocked must be boolean")


class LogisticsGraph:
    def __init__(self):
        self.adj: dict[str, list[Edge]] = {}

    def add_edge(
        self, a: str, b: str, *, cost: float, time: float,
        risk: float = 0.0, blocked: bool = False, bidirectional: bool = True,
    ) -> None:
        if any(not isinstance(node, str) or not node.strip() for node in (a, b)):
            raise ValueError("edge endpoints must be non-empty strings")
        cost = _finite_nonnegative("cost", cost)
        time = _finite_nonnegative("time", time)
        risk = _finite_nonnegative("risk", risk)
        if not isinstance(blocked, bool) or not isinstance(bidirectional, bool):
            raise ValueError("blocked and bidirectional must be booleans")
        self.adj.setdefault(a, []).append(Edge(b, float(cost), float(time), float(risk), blocked))
        if bidirectional:
            self.adj.setdefault(b, []).append(Edge(a, float(cost), float(time), float(risk), blocked))

    def route(self, start: str, goal: str, *, cost_weight: float = 1.0, time_weight: float = 1.0, risk_weight: float = 1.0):
        if any(not isinstance(node, str) or not node.strip() for node in (start, goal)):
            raise ValueError("route endpoints must be non-empty strings")
        weights = (cost_weight, time_weight, risk_weight)
        weights = tuple(_finite_nonnegative(name, weight) for name, weight in zip(
            ("cost_weight", "time_weight", "risk_weight"), weights
        ))
        if start == goal:
            return {"path": [start], "objective": 0.0, "cost": 0.0, "time": 0.0, "risk": 0.0}
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
                if not isfinite(edge_score) or not isfinite(new):
                    raise OverflowError("route objective is outside finite numeric range")
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
            if not all(isfinite(value) for value in totals.values()):
                raise OverflowError("route totals are outside finite numeric range")
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
