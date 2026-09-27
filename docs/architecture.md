# Architecture

```mermaid
flowchart LR
    X0[network] --> X1
    X1[objective weights] --> X2
    X2[edge score] --> X3
    X3[shortest-path search] --> X4
    X4[route] --> X5
    X5[cost/time/risk explanation]
```

## Graph
Nodes represent logistics locations; edges carry cost, time, and risk.

## Objective
User-selected weights convert attributes into a transparent edge score.

## Search
Dijkstra finds the lowest weighted objective path.

## Explanation
Returned route retains cost/time/risk component totals instead of only the scalar score.

## Design principle
Keep objectives decomposable so a route can be explained instead of hiding trade-offs inside one learned score.
