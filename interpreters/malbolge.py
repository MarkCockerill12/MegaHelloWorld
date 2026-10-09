"""Malbolge, following the behaviour of the original reference interpreter."""
from interpreters.common import out, read_char

MEMORY = 59049
LOAD_TABLE = (
    "+b(29e*j1VMEKLyC})8&m#~W>qxdRp0wkrUo[D7,XTcA\"lI.v%{gJh4G\\-=O@5`_3i<?Z';FNQuY]szf$!BS/|t:Pn6^Ha"
)
CIPHER_TABLE = (
    "5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@"
)
CRAZY = ((1, 0, 0), (1, 0, 2), (2, 2, 1))


def crazy(a, d):
    result, weight = 0, 1
    for _ in range(10):
        result += CRAZY[d % 3][a % 3] * weight
        a, d, weight = a // 3, d // 3, weight * 3
    return result


def load(source):
    memory, pos = [0] * MEMORY, 0
    for ch in source:
        if ch.isspace():
            continue
        code = ord(ch)
        if not 33 <= code <= 126 or LOAD_TABLE[(code - 33 + pos) % 94] not in "ji*p</vo":
            raise SyntaxError(f"invalid character {ch!r} at position {pos}")
        memory[pos] = code
        pos += 1
    if pos < 2:
        raise SyntaxError("a Malbolge program needs at least two characters")
    for i in range(pos, MEMORY):
        memory[i] = crazy(memory[i - 1], memory[i - 2])
    return memory


def run_malbolge(source):
    memory = load(source)
    a = c = d = 0
    while 33 <= memory[c] <= 126:
        instruction = LOAD_TABLE[(memory[c] - 33 + c) % 94]
        if instruction == "j":
            d = memory[d]
        elif instruction == "i":
            c = memory[d]
        elif instruction == "*":
            a = memory[d] = memory[d] // 3 + memory[d] % 3 * (MEMORY // 3)
        elif instruction == "p":
            a = memory[d] = crazy(a, memory[d])
        elif instruction == "<":
            out(chr(a % 256))
        elif instruction == "/":
            a = read_char() or MEMORY - 1
        elif instruction == "v":
            return
        if 33 <= memory[c] <= 126:
            memory[c] = ord(CIPHER_TABLE[memory[c] - 33])
        c, d = (c + 1) % MEMORY, (d + 1) % MEMORY
