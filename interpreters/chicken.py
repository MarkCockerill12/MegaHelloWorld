"""Chicken. Values follow JavaScript rules, as in the original implementation."""
import html

from interpreters.common import out

EXIT, CHICKEN, ADD, SUBTRACT, MULTIPLY, COMPARE, LOAD, STORE, JUMP, CHAR = range(10)


def number(value):
    """JavaScript-style conversion to a number; NaN is represented by None."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    try:
        return int(str(value).strip() or 0)
    except ValueError:
        return None


def text(value):
    if value is None:
        return "undefined"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def add(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return text(a) + text(b)
    return arithmetic(a, b, lambda x, y: x + y)


def arithmetic(a, b, operation):
    a, b = number(a), number(b)
    return "NaN" if a is None or b is None else operation(a, b)


def element(source, index):
    index = number(index)
    if index is None or not 0 <= index < len(source):
        return None
    return source[index]


def run_chicken(source, user_input=""):
    lines = source.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    for line in lines:
        if line.replace("chicken", "").strip():
            raise SyntaxError(f"only 'chicken' is allowed, found: {line.strip()[:30]!r}")

    # The stack holds a reference to itself, the input, the code and then the data
    stack = [None, user_input] + [line.count("chicken") for line in lines] + [EXIT]
    pc = 2
    while pc < len(stack):
        opcode = stack[pc]
        pc += 1
        if opcode == EXIT:
            break
        if opcode == CHICKEN:
            stack.append("chicken")
        elif opcode == ADD:
            b, a = stack.pop(), stack.pop()
            stack.append(add(a, b))
        elif opcode == SUBTRACT:
            b, a = stack.pop(), stack.pop()
            stack.append(arithmetic(a, b, lambda x, y: x - y))
        elif opcode == MULTIPLY:
            b, a = stack.pop(), stack.pop()
            stack.append(arithmetic(a, b, lambda x, y: x * y))
        elif opcode == COMPARE:
            b, a = stack.pop(), stack.pop()
            stack.append(text(a) == text(b))
        elif opcode == LOAD:
            source_index = stack[pc]
            pc += 1
            index = stack.pop()
            stack.append(element(stack if source_index == 0 else stack[source_index], index))
        elif opcode == STORE:
            address, value = stack.pop(), stack.pop()
            stack.extend([None] * (address + 1 - len(stack)))
            stack[address] = value
        elif opcode == JUMP:
            offset, condition = stack.pop(), stack.pop()
            if condition:
                pc += offset
        elif opcode == CHAR:
            stack.append(f"&#{stack.pop()};")
        else:
            stack.append(opcode - 10)
    # The original prints into a web page, so character entities become characters
    out(html.unescape(text(stack[-1])))
