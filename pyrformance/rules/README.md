# Rules

## Rejected

There are some ideas that sounded like being faster but experments showed that it's not true.

+ `{**a, **b}` gives about the same performance as `a | b`.
+ `[*a]` is faster than `list(a)` but IMHO less readable.
