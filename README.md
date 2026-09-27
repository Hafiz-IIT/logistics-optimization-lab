# Logistics Optimization Lab

> **A transparent multi-objective routing sandbox for cost, time, and operational risk.**

EXIM/logistics decisions rarely optimize one scalar. Routes trade transport cost, transit time, disruption risk, and operational constraints. This repository provides an inspectable graph baseline before adding learned or real-data methods.

## Implemented
- weighted logistics graph
- bidirectional edge support
- cost/time/risk edge attributes
- configurable objective weights
- Dijkstra routing
- route reconstruction
- component totals
- no-route handling

## Repository map
- `logistics_optimization_lab.py` — core implementation
- `tests/` — deterministic tests
- `examples/` — sample case
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments + research lineage
- `STATUS.md` — claims boundary
- `CITATION.cff` — citation metadata

## Run
```bash
python -m unittest discover -s tests -v
python logistics_optimization_lab.py
```

## Pipeline
**network → objective weights → edge score → shortest-path search → route → cost/time/risk explanation**

## Research lineage
This consolidates older smart-logistics, cargo-routing, scheduling, cost-optimization, and port/logistics capstone themes into one defensible algorithmic lab.

## Evaluation direction
Benchmark how selected paths change across objective weights, network disruption, and risk penalties; later compare against Pareto-frontier or constrained optimization methods.

## Maturity
**Research prototype.** Synthetic network only. No real fleet telemetry, carrier rates, map API, customs timings, or production dispatch is claimed.
