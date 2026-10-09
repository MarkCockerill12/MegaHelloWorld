"""Befunge-93."""
import random

from interpreters.common import out, read_char, read_number


def run_befunge(source):
    width, height = 80, 25
    grid = [[" "] * width for _ in range(height)]
    for y, line in enumerate(source.split("\n")[:height]):
        for x, ch in enumerate(line[:width]):
            grid[y][x] = ch

    stack = []
    x = y = 0
    dx, dy = 1, 0
    string_mode = False

    def pop():
        return stack.pop() if stack else 0

    binary = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b if b else 0,
        "%": lambda a, b: a % b if b else 0,
        "`": lambda a, b: int(a > b),
    }
    directions = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

    while True:
        ch = grid[y][x]
        if string_mode:
            if ch == '"':
                string_mode = False
            else:
                stack.append(ord(ch))
        elif ch == '"':
            string_mode = True
        elif ch.isdigit():
            stack.append(int(ch))
        elif ch in binary:
            b, a = pop(), pop()
            stack.append(binary[ch](a, b))
        elif ch in directions:
            dx, dy = directions[ch]
        elif ch == "?":
            dx, dy = random.choice(list(directions.values()))
        elif ch == "!":
            stack.append(int(pop() == 0))
        elif ch == "_":
            dx, dy = (-1, 0) if pop() else (1, 0)
        elif ch == "|":
            dx, dy = (0, -1) if pop() else (0, 1)
        elif ch == ":":
            top = pop()
            stack.extend([top, top])
        elif ch == "\\":
            b, a = pop(), pop()
            stack.extend([b, a])
        elif ch == "$":
            pop()
        elif ch == ".":
            out(f"{pop()} ")
        elif ch == ",":
            out(chr(pop()))
        elif ch == "#":
            x, y = (x + dx) % width, (y + dy) % height
        elif ch == "g":
            gy, gx = pop(), pop()
            inside = 0 <= gx < width and 0 <= gy < height
            stack.append(ord(grid[gy][gx]) if inside else 0)
        elif ch == "p":
            py, px, value = pop(), pop(), pop()
            if 0 <= px < width and 0 <= py < height:
                grid[py][px] = chr(value % 256)
        elif ch == "&":
            stack.append(read_number())
        elif ch == "~":
            stack.append(read_char())
        elif ch == "@":
            return
        x, y = (x + dx) % width, (y + dy) % height
