from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import NoReturn, TextIO


def main(argv: list[str], stdout: TextIO) -> int:
    rules_path = Path(__file__).parent / 'rules'
    cmd = [
        sys.executable, '-m', 'semgrep', 'scan',
        '--disable-version-check',
        '--config', str(rules_path),
        *argv,
    ]
    result = subprocess.run(cmd, stdout=stdout)
    return result.returncode


def entrypoint() -> NoReturn:
    code = main(sys.argv[1:], sys.stdout)
    sys.exit(code)
