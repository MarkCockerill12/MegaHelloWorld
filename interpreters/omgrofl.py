"""Omgrofl."""
import re
import time

from interpreters.common import out, read_char

OMGROFL_VARIABLE = re.compile(r"^lo+l$")


class OmgroflExit(Exception):
    pass


class OmgroflBreak(Exception):
    pass


def parse_omgrofl(lines, pos=0, nested=False):
    """Turn lines into a tree: plain statements, plus (header, body) blocks."""
    block = []
    while pos < len(lines):
        words = lines[pos]
        pos += 1
        if words[0] == "brb":
            if not nested:
                raise SyntaxError("brb without a block to close")
            return block, pos
        if words[0] in ("wtf", "rtfm", "4"):
            body, pos = parse_omgrofl(lines, pos, True)
            block.append((words, body))
        else:
            block.append((words, None))
    if nested:
        raise SyntaxError("block is missing its brb")
    return block, pos


def run_omgrofl(source):
    lines = []
    for line in source.lower().split("\n"):
        words = line.split("w00t")[0].split()
        if words:
            lines.append(words)
    tree, _ = parse_omgrofl(lines)
    variables, stack = {}, []

    def name(word):
        if not OMGROFL_VARIABLE.match(word):
            raise SyntaxError(f"{word!r} is not a variable (use lol, lool, loool...)")
        return word

    def value(word):
        if OMGROFL_VARIABLE.match(word):
            return variables.get(word, 0)
        return int(word) % 256

    def condition(words):
        negate = "nope" in words
        words = [w for w in words if w != "nope"]
        left, right = value(words[0]), value(words[3])
        result = left == right if words[2] == "liek" else left > right
        return result != negate

    def execute(block):
        for words, body in block:
            command = words[0]
            if command == "wtf":
                if condition(words[1:]):
                    execute(body)
            elif command == "rtfm":
                try:
                    while True:
                        execute(body)
                except OmgroflBreak:
                    pass
            elif command == "4":
                counter, start, end = name(words[1]), value(words[3]), value(words[5])
                step = 1 if end >= start else -1
                try:
                    for current in range(start, end, step):
                        variables[counter] = current
                        execute(body)
                except OmgroflBreak:
                    pass
            elif command == "tldr":
                raise OmgroflBreak
            elif command == "stfu":
                raise OmgroflExit
            elif command == "lmao":
                variables[name(words[1])] = (value(words[1]) + 1) % 256
            elif command == "roflmao":
                variables[name(words[1])] = (value(words[1]) - 1) % 256
            elif command == "rofl":
                out(chr(value(words[1])))
            elif command == "stfw":
                variables[name(words[1])] = read_char() % 256
            elif command == "n00b":
                stack.append(value(words[1]))
            elif command == "l33t":
                variables[name(words[1])] = stack.pop() if stack else 0
            elif command == "haxor":
                variables[name(words[1])] = stack.pop(0) if stack else 0
            elif command == "afk":
                time.sleep(value(words[1]) / 1000)
            elif len(words) == 3 and words[1] == "iz":
                variables[name(command)] = value(words[2])
            else:
                raise SyntaxError(f"unknown Omgrofl statement: {' '.join(words)}")

    try:
        execute(tree)
    except OmgroflExit:
        pass
