"""Output and input helpers shared by the interpreters."""
import sys


def out(text):
    sys.stdout.write(text)


def read_char():
    ch = sys.stdin.read(1)
    return ord(ch) if ch else 0


def read_number():
    line = sys.stdin.readline().strip()
    return int(line) if line else 0
