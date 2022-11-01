from __future__ import annotations

import json
from pathlib import Path

import pytest

from pyrformance import main


def parse_output(stdout: str) -> list[dict]:
    print(stdout)
    last_line = stdout.splitlines()[-1]
    parsed = json.loads(last_line)
    assert parsed['errors'] == []
    return parsed['results']


@pytest.mark.parametrize('code, expected', [
    ('"oh hi mark".split()[0]', 'str-split-maxsplit'),
    ('"oh hi mark".split(" ")[0]', 'str-split-maxsplit'),
    ('"oh hi mark".split()[-1]', 'str-split-maxsplit'),
    ('"oh hi mark".split(" ")[-1]', 'str-split-maxsplit'),
    ('"oh hi mark".rsplit()[-1]', 'str-split-maxsplit'),
    ('"oh hi mark".rsplit(" ")[-1]', 'str-split-maxsplit'),

    ('"oh hi mark".split()', None),
    ('"oh hi mark".split(" ")', None),
    ('"oh hi mark".rsplit()', None),
    ('"oh hi mark".rsplit(" ")', None),
    ('"oh hi mark".split()[x]', None),
    ('"oh hi mark".split(maxsplit=1)[0]', None),

    ('x in set(y)', 'set-contains'),
    ('1 in set(y)', 'set-contains'),
    ('1 in set(x + y)', 'set-contains'),
    ('1 in y', None),

    ('any(set(x))', 'any-all-laziness'),
    ('all(set(x))', 'any-all-laziness'),
    ('any(list(x))', 'any-all-laziness'),
    ('all(list(x))', 'any-all-laziness'),
    ('any(tuple(x))', 'any-all-laziness'),
    ('all(tuple(x))', 'any-all-laziness'),

    ('"hello" + a + b', 'str-concat'),

    ('{**a, **b}', 'dict-merge'),

    ('import re\nre.match("[0-9]", x)', 're-compile'),
    ('import re\nre.finditer("[0-9]", x)', 're-compile'),
    ('import re\nre.match(pattern, x)', None),
    ('import re\nre.compile("[0-9]")', None),

    ('list(list(x))', 'double-call'),
    ('list(set(x))', None),

    ('(abs(x) for x in y)', 'map'),
    ('(abs(x) for x in y if x)', None),
])
def test_rule_violation(code: str, expected: str | None, tmp_path: Path) -> None:
    file_path = tmp_path / 'example.py'
    file_path.write_text(f'{code}\n')
    print(file_path.read_text())
    out_path = tmp_path / 'result.txt'
    with out_path.open('w') as stdout:
        main(['--error', '--json', str(file_path)], stdout)
    actual = parse_output(out_path.read_text())
    if expected is None:
        assert len(actual) == 0
    else:
        assert len(actual) == 1
        assert actual[0]['check_id'] == f'pyrformance.rules.{expected}'
