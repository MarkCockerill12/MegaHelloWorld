"""FALSE (no inline assembly)."""
from interpreters.common import out, read_char

PICK = "øO"
FLUSH = "ßB"


def parse_false(code, pos=0, nested=False):
    """Turn source into a list of tokens; a lambda becomes a nested list."""
    tokens = []
    while pos < len(code):
        ch = code[pos]
        pos += 1
        if ch == "{":
            pos = code.index("}", pos) + 1
        elif ch == '"':
            end = code.index('"', pos)
            tokens.append(("string", code[pos:end]))
            pos = end + 1
        elif ch == "'":
            tokens.append(("number", ord(code[pos])))
            pos += 1
        elif ch.isdigit():
            start = pos - 1
            while pos < len(code) and code[pos].isdigit():
                pos += 1
            tokens.append(("number", int(code[start:pos])))
        elif ch == "[":
            body, pos = parse_false(code, pos, True)
            tokens.append(("lambda", body))
        elif ch == "]":
            if not nested:
                raise SyntaxError("] without a matching [")
            return tokens, pos
        elif "a" <= ch <= "z":
            tokens.append(("variable", ch))
        elif not ch.isspace():
            tokens.append(("op", ch))
    if nested:
        raise SyntaxError("[ without a matching ]")
    return tokens, pos


def run_false(source):
    program, _ = parse_false(source)
    stack, variables = [], {}
    binary = {
        "+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b), "&": lambda a, b: a & b, "|": lambda a, b: a | b,
        "=": lambda a, b: -int(a == b), ">": lambda a, b: -int(a > b),
    }

    def execute(tokens):
        for kind, value in tokens:
            if kind == "string":
                out(value)
            elif kind != "op":
                stack.append(value)
            elif value in binary:
                b, a = stack.pop(), stack.pop()
                stack.append(binary[value](a, b))
            elif value == "_":
                stack.append(-stack.pop())
            elif value == "~":
                stack.append(~stack.pop())
            elif value == "$":
                stack.append(stack[-1])
            elif value == "%":
                stack.pop()
            elif value == "\\":
                stack[-1], stack[-2] = stack[-2], stack[-1]
            elif value == "@":
                stack.append(stack.pop(-3))
            elif value in PICK:
                stack.append(stack[-1 - stack.pop()])
            elif value == ":":
                variables[stack.pop()] = stack.pop()
            elif value == ";":
                stack.append(variables[stack.pop()])
            elif value == "!":
                execute(stack.pop())
            elif value == "?":
                body, condition = stack.pop(), stack.pop()
                if condition:
                    execute(body)
            elif value == "#":
                body, condition = stack.pop(), stack.pop()
                while True:
                    execute(condition)
                    if not stack.pop():
                        break
                    execute(body)
            elif value == ".":
                out(str(stack.pop()))
            elif value == ",":
                out(chr(stack.pop()))
            elif value == "^":
                stack.append(read_char() or -1)
            elif value not in FLUSH:
                raise SyntaxError(f"unknown FALSE command {value!r}")

    execute(program)
