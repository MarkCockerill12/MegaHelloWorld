"""Unlambda (s, k, i, v, r and .x; no c, d, e or input)."""
from interpreters.common import out


def parse_unlambda(code, pos=0):
    while pos < len(code) and code[pos].isspace():
        pos += 1
    if pos >= len(code):
        raise SyntaxError("unexpected end of Unlambda program")
    ch = code[pos]
    if ch == "`":
        function, pos = parse_unlambda(code, pos + 1)
        argument, pos = parse_unlambda(code, pos)
        return ("apply", function, argument), pos
    if ch == ".":
        return ("print", code[pos + 1]), pos + 2
    if ch == "r":
        return ("print", "\n"), pos + 1
    if ch in "skiv":
        return (ch,), pos + 1
    raise SyntaxError(f"unsupported Unlambda character {ch!r}")


def apply_unlambda(function, argument):
    kind = function[0]
    if kind == "print":
        out(function[1])
        return argument
    if kind == "i":
        return argument
    if kind == "v":
        return function
    if kind == "k":
        return ("k1", argument)
    if kind == "k1":
        return function[1]
    if kind == "s":
        return ("s1", argument)
    if kind == "s1":
        return ("s2", function[1], argument)
    first = apply_unlambda(function[1], argument)
    return apply_unlambda(first, apply_unlambda(function[2], argument))


def eval_unlambda(node):
    if node[0] != "apply":
        return node
    function = eval_unlambda(node[1])
    return apply_unlambda(function, eval_unlambda(node[2]))


def run_unlambda(source):
    code = "\n".join(line.split("#")[0] for line in source.split("\n")).strip()
    tree, pos = parse_unlambda(code)
    if code[pos:].strip():
        raise SyntaxError("trailing characters after Unlambda program")
    eval_unlambda(tree)
