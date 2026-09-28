# Logistics Optimization Lab

> Multi-objective logistics routing sandbox balancing monetary cost, travel time and operational risk.

## Status
**Reproducible simulation/research prototype** with tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Operational routing rarely optimizes one metric. Cost, time and risk compete, and route choice should be explainable when priorities change.

## Architecture
Weighted logistics graph → cost/time/risk edge attributes → configurable objective weights → shortest-path solver → path plus component totals.

## Run
```bash
python -m unittest discover -s tests -v
python logistics_optimization_lab.py
```

## Implemented
- Weighted graph model
- Bidirectional edge support
- Cost/time/risk objective
- Dijkstra routing
- Route component totals
- No-route handling
- Tests and CI

## Research lineage
- *Smart Urban Infrastructures: AI-Enabled City Optimization*
- *AI for Climate Change: Modeling Micro-Level Energy Efficiency*
- *Bridging Classical Control and Modern AI: A Unified Framework for Automated Agents*

## Evaluation
Current tests verify objective-sensitive route changes and unreachable cases; future work adds stochastic and constrained routing.

## Limitations
- Synthetic graph only
- No live maps/traffic
- Single-vehicle path problem
- No time windows or capacity constraints yet

## License
MIT.
