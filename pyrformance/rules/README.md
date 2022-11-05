# Rules

## Rejected

There are some ideas that sounded like being faster but experments showed that it's not true.

+ `{**a, **b}` gives about the same performance as `a | b`.
+ `[*a]` is faster than `list(a)` but IMHO less readable.
+ `dict.pop(key)` is equivalent to `del dict[key]` when is used as a statement, and the latter is faster. However, there is no way in semgrep to match statements but not expressions.
