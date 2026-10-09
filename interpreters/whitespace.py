"""Whitespace."""
from interpreters.common import out, read_char, read_number

WS_COMMANDS = {
    "  ": ("push", "number"), " \n ": ("dup", None), " \n\t": ("swap", None),
    " \n\n": ("drop", None), " \t ": ("copy", "number"), " \t\n": ("slide", "number"),
    "\t   ": ("add", None), "\t  \t": ("sub", None), "\t  \n": ("mul", None),
    "\t \t ": ("div", None), "\t \t\t": ("mod", None),
    "\t\t ": ("store", None), "\t\t\t": ("retrieve", None),
    "\n  ": ("label", "label"), "\n \t": ("call", "label"), "\n \n": ("jump", "label"),
    "\n\t ": ("jz", "label"), "\n\t\t": ("jneg", "label"), "\n\t\n": ("ret", None),
    "\n\n\n": ("end", None),
    "\t\n  ": ("outchar", None), "\t\n \t": ("outnum", None),
    "\t\n\t ": ("readchar", None), "\t\n\t\t": ("readnum", None),
}


def parse_whitespace(source):
    code = "".join(c for c in source if c in " \t\n")
    program, pos = [], 0
    while pos < len(code):
        for prefix, (name, param) in WS_COMMANDS.items():
            if code.startswith(prefix, pos):
                break
        else:
            raise SyntaxError(f"unknown Whitespace command at offset {pos}")
        pos += len(prefix)
        arg = None
        if param:
            end = code.index("\n", pos)
            arg = code[pos:end]
            pos = end + 1
            if param == "number":
                digits = arg[1:].replace(" ", "0").replace("\t", "1")
                arg = int(digits or "0", 2) * (-1 if arg[:1] == "\t" else 1)
        program.append((name, arg))
    return program


def run_whitespace(source):
    program = parse_whitespace(source)
    labels = {arg: pos for pos, (name, arg) in enumerate(program) if name == "label"}
    stack, heap, calls, pc = [], {}, [], 0
    arithmetic = {
        "add": lambda a, b: a + b, "sub": lambda a, b: a - b, "mul": lambda a, b: a * b,
        "div": lambda a, b: a // b, "mod": lambda a, b: a % b,
    }
    while pc < len(program):
        name, arg = program[pc]
        pc += 1
        if name == "push":
            stack.append(arg)
        elif name == "dup":
            stack.append(stack[-1])
        elif name == "swap":
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif name == "drop":
            stack.pop()
        elif name == "copy":
            stack.append(stack[-1 - arg])
        elif name == "slide":
            top = stack.pop()
            del stack[len(stack) - arg:]
            stack.append(top)
        elif name in arithmetic:
            b, a = stack.pop(), stack.pop()
            stack.append(arithmetic[name](a, b))
        elif name == "store":
            value, address = stack.pop(), stack.pop()
            heap[address] = value
        elif name == "retrieve":
            stack.append(heap.get(stack.pop(), 0))
        elif name == "call":
            calls.append(pc)
            pc = labels[arg]
        elif name == "jump":
            pc = labels[arg]
        elif name == "jz":
            if stack.pop() == 0:
                pc = labels[arg]
        elif name == "jneg":
            if stack.pop() < 0:
                pc = labels[arg]
        elif name == "ret":
            pc = calls.pop()
        elif name == "end":
            return
        elif name == "outchar":
            out(chr(stack.pop()))
        elif name == "outnum":
            out(str(stack.pop()))
        elif name == "readchar":
            heap[stack.pop()] = read_char()
        elif name == "readnum":
            heap[stack.pop()] = read_number()
