"""Glass, with the built-in classes A, S, V, O and I."""
import math
import re
import sys

from interpreters.common import out

TOKEN = re.compile(r"""
    \s+ | '[^']*'
  | \((?P<paren>[^)]*)\)
  | "(?P<string>[^"]*)"
  | <(?P<number>[^>]*)>
  | (?P<char>.)
""", re.VERBOSE | re.DOTALL)


class Name(str):
    """A variable name on the stack, as opposed to a string value."""


class Return(Exception):
    pass


class Instance:
    def __init__(self, cls):
        self.cls, self.fields = cls, {}


def tokenize(source):
    for match in TOKEN.finditer(source):
        if match.group("paren") is not None:
            yield ("ref", match.group("paren"))
        elif match.group("string") is not None:
            yield ("string", match.group("string").replace("\\n", "\n"))
        elif match.group("number") is not None:
            value = float(match.group("number"))
            yield ("number", int(value) if value.is_integer() else value)
        elif match.group("char") is not None:
            ch = match.group("char")
            yield ("ref", ch) if ch.isalnum() else ("op", ch)


def parse_glass(source):
    tokens = list(tokenize(source)) + [("end", None)]
    classes, pos = {}, 0
    while tokens[pos][0] != "end":
        if tokens[pos] != ("op", "{"):
            raise SyntaxError("expected a class definition")
        class_name, functions = tokens[pos + 1][1], {}
        pos += 2
        while tokens[pos] != ("op", "}"):
            if tokens[pos] != ("op", "["):
                raise SyntaxError(f"expected a function in class {class_name}")
            function_name = tokens[pos + 1][1]
            functions[function_name], pos = parse_function(tokens, pos + 2)
        classes[class_name] = functions
        pos += 1
    return classes


def parse_function(tokens, pos, closer="]"):
    block = []
    while tokens[pos] != ("op", closer):
        kind, value = tokens[pos]
        if kind == "end":
            raise SyntaxError(f"missing {closer}")
        pos += 1
        if (kind, value) == ("op", "/"):
            loop_name = tokens[pos][1]
            body, pos = parse_function(tokens, pos + 1, "\\")
            block.append(("loop", loop_name, body))
        else:
            block.append((kind, value, None))
    return block, pos + 1


def builtins(stack, generated):
    def pop2():
        b, a = stack.pop(), stack.pop()
        return a, b

    def binary(operation):
        def run():
            a, b = pop2()
            result = operation(a, b)
            stack.append(int(result) if isinstance(result, bool) else result)
        return run

    def divide_string():
        string, position = pop2()
        stack.extend([string[:position], string[position:]])

    def set_index():
        char = stack.pop()
        string, position = pop2()
        stack.append(string[:position] + char + string[position + 1:])

    def new_variable():
        generated[0] += 1
        stack.append(Name(f"Generated{generated[0]}"))

    def output_number():
        value = stack.pop()
        out(str(int(value) if float(value).is_integer() else value))

    def read_line():
        stack.append(sys.stdin.readline())

    def read_one():
        stack.append(sys.stdin.read(1))

    return {
        "A": {
            "a": binary(lambda a, b: a + b), "s": binary(lambda a, b: a - b),
            "m": binary(lambda a, b: a * b), "d": binary(lambda a, b: a / b),
            "mod": binary(lambda a, b: a % b), "f": lambda: stack.append(math.floor(stack.pop())),
            "e": binary(lambda a, b: a == b), "ne": binary(lambda a, b: a != b),
            "lt": binary(lambda a, b: a < b), "le": binary(lambda a, b: a <= b),
            "gt": binary(lambda a, b: a > b), "ge": binary(lambda a, b: a >= b),
        },
        "S": {
            "l": lambda: stack.append(len(stack.pop())),
            "i": binary(lambda string, position: string[position]),
            "si": set_index, "a": binary(lambda a, b: str(a) + str(b)), "d": divide_string,
            "e": binary(lambda a, b: a == b),
            "ns": lambda: stack.append(chr(int(stack.pop()))),
            "sn": lambda: stack.append(ord(stack.pop())),
        },
        "V": {"n": new_variable, "d": lambda: stack.pop()},
        "O": {"o": lambda: out(str(stack.pop())), "on": output_number},
        "I": {"l": read_line, "c": read_one, "e": lambda: stack.append(0)},
    }


def run_glass(source):
    classes = parse_glass(source)
    stack, global_vars, generated = [], {}, [0]
    native = builtins(stack, generated)

    def scope(name, self, local_vars):
        if name.startswith("_"):
            return local_vars
        return global_vars if name[:1].isupper() else self.fields

    def lookup(name, self, local_vars):
        variables = scope(name, self, local_vars)
        if name not in variables and (name in classes or name in native):
            return ("class", name)
        return variables[name]

    def instantiate(class_name):
        instance = Instance(class_name)
        if "c__" in classes.get(class_name, {}):
            call(instance, "c__")
        return instance

    def call(instance, function_name):
        if instance.cls in native:
            native[instance.cls][function_name]()
            return
        try:
            execute(classes[instance.cls][function_name], instance, {})
        except Return:
            pass

    def execute(block, self, local_vars):
        for kind, value, body in block:
            if kind == "loop":
                while lookup(value, self, local_vars):
                    execute(body, self, local_vars)
            elif kind == "ref":
                stack.append(stack[-1 - int(value)] if value.isdigit() else Name(value))
            elif kind != "op":
                stack.append(value)
            elif value == ",":
                stack.pop()
            elif value == "^":
                raise Return
            elif value == "=":
                assigned, name = stack.pop(), stack.pop()
                scope(name, self, local_vars)[name] = assigned
            elif value == "!":
                class_name, name = stack.pop(), stack.pop()
                scope(name, self, local_vars)[name] = instantiate(lookup(class_name, self, local_vars)[1])
            elif value == ".":
                function_name, name = stack.pop(), stack.pop()
                stack.append((lookup(name, self, local_vars), str(function_name)))
            elif value == "?":
                call(*stack.pop())
            elif value == "*":
                stack.append(lookup(stack.pop(), self, local_vars))
            elif value == "$":
                name = stack.pop()
                scope(name, self, local_vars)[name] = self
            else:
                raise SyntaxError(f"unknown Glass command {value!r}")

    if "m" not in classes.get("M", {}):
        raise SyntaxError("a Glass program needs a class M with a function m")
    call(instantiate("M"), "m")
