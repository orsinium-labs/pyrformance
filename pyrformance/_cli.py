from __future__ import annotations
from pathlib import Path
import sys
import subprocess
from typing import NoReturn, TextIO


def main(argv: list[str], stdout: TextIO) -> int:
    rules_path = Path(__file__).parent / 'rules'
    result = subprocess.run([
        sys.executable, '-m', 'semgrep', 'scan',
        '--config', str(rules_path),
        *argv,
    ])
    return result.returncode


def entrypoint() -> NoReturn:
    code = main(sys.argv[1:], sys.stdout)
    sys.exit(code)
