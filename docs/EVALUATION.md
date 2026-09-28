# Evaluation

## Question
How do explicit cost/time/risk trade-offs change routing decisions under operational disruptions?

## Metrics
- Weighted objective
- Total cost
- Total time
- Total risk
- Route stability under weight changes

## Falsification
- The solver chooses a route with a higher objective when a lower one exists.
- Reported totals disagree with traversed edges.
- Unreachable destinations return a fake route.
