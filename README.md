# pyrformance

Linter that makes your Python code faster.

Pyrformance is a collection [semgrep](https://semgrep.dev/) rules and a thin wrapper on top of [semgrep CLI](https://github.com/returntocorp/semgrep) for a simple way of running these rules. All rules are non-opinionated and performance-focused.

Features:

+ **Non-opinionated**. If pyrformance reports something, changing it will make your code faster. That's it. It won't tell you to change something just because it's a "pythonic", consistent, or whatever else.
+ **Benchmarked**. For each rule, we have a [true-north](https://github.com/orsinium-labs/true-north)-powered benchmark that shows that the rule indeed makes code faster. We don't play guessing or advice something just because a random Medium article says so.
+ **Tested**. We have tests for each rule, which is quite unusual for semgrep rules you can find in the wild.
+ **Never compromises readability**. We do our best to not recommend any changes that would make the code less readable, even if that would be faster.

## Installation

```bash
python3 -m pip install pyrformance
```

## Usage

```bash
python3 -m pyrformance ./your_project/
```

## License

+ The code and rules in pyrformance are licensed under [MIT](./LICENSE).
+ [semgrep](https://github.com/returntocorp/semgrep) is licensed under [GNU LGPL](https://github.com/returntocorp/semgrep/blob/develop/LICENSE).

If you use pyrformance, you should accept both licenses.
