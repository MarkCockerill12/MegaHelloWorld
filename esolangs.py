"""Small interpreters for esoteric languages that have no packaged toolchain.

Usage: python3 esolangs.py <language> <file>
"""
import sys

from interpreters.befunge import run_befunge
from interpreters.brainfuck import run_arch, run_brainfuck, run_ook
from interpreters.chicken import run_chicken
from interpreters.false import run_false
from interpreters.glass import run_glass
from interpreters.malbolge import run_malbolge
from interpreters.omgrofl import run_omgrofl
from interpreters.piet import run_piet
from interpreters.unlambda import run_unlambda
from interpreters.whitespace import run_whitespace
from interpreters.zombie import run_zombie

LANGUAGES = {
    "arch": run_arch,
    "befunge": run_befunge,
    "brainfuck": run_brainfuck,
    "chicken": run_chicken,
    "false": run_false,
    "glass": run_glass,
    "malbolge": run_malbolge,
    "omgrofl": run_omgrofl,
    "ook": run_ook,
    "piet": run_piet,
    "unlambda": run_unlambda,
    "whitespace": run_whitespace,
    "zombie": run_zombie,
}
# Languages whose programs are images rather than text
BINARY = {"piet"}


def read_source(language, path):
    if language in BINARY:
        with open(path, "rb") as handle:
            return handle.read()
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read().replace("\r\n", "\n")


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in LANGUAGES:
        print(f"Usage: python3 esolangs.py [{' | '.join(LANGUAGES)}] <file>", file=sys.stderr)
        return 2
    language = sys.argv[1]
    try:
        LANGUAGES[language](read_source(language, sys.argv[2]))
    except (SyntaxError, IndexError, KeyError, ValueError, ZeroDivisionError, TypeError) as error:
        sys.stdout.flush()
        print(f"{language} error: {error!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
