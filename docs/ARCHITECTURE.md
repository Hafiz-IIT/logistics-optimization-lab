# Architecture

Weighted logistics graph → cost/time/risk edge attributes → configurable objective weights → shortest-path solver → path plus component totals.

## Invariants
1. Blocked/unavailable edges must not be used.
2. Reported totals must correspond to the chosen path.
3. Changing objective weights may change route but not underlying edge data.
