# Logistics Optimization Lab

A small, reproducible sandbox for multi-objective route selection in logistics networks.

## Implemented
- weighted graph representation
- Dijkstra shortest path
- configurable cost / time / risk objective weights
- blocked-edge support
- route explanation with component totals
- deterministic tests

## Run
```bash
python -m unittest discover -s tests -v
python logistics_optimization_lab.py
```

This is a simulation/algorithm lab using synthetic networks, not a production fleet-routing system or real carrier data.
