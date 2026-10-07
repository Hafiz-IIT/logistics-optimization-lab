# Logistics Optimization Lab

<p align="center"><strong>Routing Under Cost, Time and Risk Trade-offs</strong><br/><sub>A transparent multi-objective logistics simulation laboratory.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20simulation-blue" alt="Simulation"/> <img src="https://img.shields.io/badge/objectives-cost%20%7C%20time%20%7C%20risk-orange" alt="Objectives"/></p>

## Question

**What happens when the “best” logistics route depends on which operational objective matters most?**

```
Network
 ↓
edge cost + time + risk
 ↓
objective / Pareto analysis
 ↓
candidate routes
 ↓
trade-off decision
```

## Try it

```bash
python logistics_optimization_lab.py
python -m unittest discover -s tests -v
```

The second-stage `pareto_routes.py` exposes non-dominated routes rather than collapsing everything into one arbitrary weight.

## Implemented

- weighted logistics graph
- bidirectional edges
- cost/time/risk objectives
- Dijkstra baseline
- route component totals
- Pareto-front analysis
- no-route handling
- deterministic CI

## Research boundary

This is a simulation laboratory. It does not claim optimization of a real carrier, port or fleet.

Related: [Port Operations Simulator](https://github.com/Hafiz-IIT/port-operations-simulator) · [Multi-Agent Logistics Simulator](https://github.com/Hafiz-IIT/multi-agent-logistics-sim) · [Traffic Incident Routing Lab](https://github.com/Hafiz-IIT/traffic-incident-routing-lab)
