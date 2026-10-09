"""Brainfuck and its word-substitution dialects (Ook!, I Use Arch Btw)."""
import re

from interpreters.common import out, read_char


def run_brainfuck(code):
    code = [c for c in code if c in "><+-.,[]"]
    jumps, stack = {}, []
    for pos, op in enumerate(code):
        if op == "[":
            stack.append(pos)
        elif op == "]":
            if not stack:
                raise SyntaxError("unmatched ]")
            start = stack.pop()
            jumps[start], jumps[pos] = pos, start
    if stack:
        raise SyntaxError("unmatched [")

    tape, ptr, pc = [0] * 30000, 0, 0
    while pc < len(code):
        op = code[pc]
        if op == ">":
            ptr = (ptr + 1) % len(tape)
        elif op == "<":
            ptr = (ptr - 1) % len(tape)
        elif op == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif op == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif op == ".":
            out(chr(tape[ptr]))
        elif op == ",":
            tape[ptr] = read_char() % 256
        elif (op == "[" and tape[ptr] == 0) or (op == "]" and tape[ptr] != 0):
            pc = jumps[pc]
        pc += 1


OOK = {
    (".", "?"): ">", ("?", "."): "<", (".", "."): "+", ("!", "!"): "-",
    ("!", "."): ".", (".", "!"): ",", ("!", "?"): "[", ("?", "!"): "]",
}

ARCH = {
    "i": ">", "use": "<", "arch": "+", "linux": "-",
    "btw": ".", "by": ",", "the": "[", "way": "]",
}


def run_ook(source):
    marks = re.findall(r"Ook([.?!])", source)
    if len(marks) % 2:
        raise SyntaxError("odd number of Ook tokens")
    run_brainfuck("".join(OOK[pair] for pair in zip(marks[::2], marks[1::2])))


def run_arch(source):
    run_brainfuck("".join(ARCH.get(word, "") for word in source.split()))
