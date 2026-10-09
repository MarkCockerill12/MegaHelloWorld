"""Piet, reading the program from a PNG image (one pixel per codel)."""
import struct
import zlib

from interpreters.common import out, read_char, read_number

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
CHANNELS = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
HUES = [(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1)]
LIGHTNESS = [(255, 192), (255, 0), (192, 0)]
COLOURS = {
    tuple(high if bit else low for bit in mask): (hue, light)
    for light, (high, low) in enumerate(LIGHTNESS)
    for hue, mask in enumerate(HUES)
}
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def paeth(left, up, corner):
    estimate = left + up - corner
    d_left, d_up, d_corner = abs(estimate - left), abs(estimate - up), abs(estimate - corner)
    if d_left <= d_up and d_left <= d_corner:
        return left
    return up if d_up <= d_corner else corner


def unfilter(raw, width, height, size):
    """Undo the PNG scanline filters; size is the number of bytes per pixel."""
    stride = width * size
    rows, previous, pos = [], bytearray(stride), 0
    for _ in range(height):
        kind, line = raw[pos], bytearray(raw[pos + 1:pos + 1 + stride])
        pos += 1 + stride
        for i in range(stride):
            left = line[i - size] if i >= size else 0
            corner = previous[i - size] if i >= size else 0
            predictor = (0, left, previous[i], (left + previous[i]) // 2, paeth(left, previous[i], corner))[kind]
            line[i] = (line[i] + predictor) % 256
        rows.append(line)
        previous = line
    return rows


def read_png(data):
    """Return the image as rows of (r, g, b) tuples. 8-bit, non-interlaced only."""
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file")
    pos, compressed, palette, header = 8, b"", [], None
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        if kind == b"IHDR":
            header = struct.unpack(">IIBBBBB", body)
        elif kind == b"PLTE":
            palette = [tuple(body[i:i + 3]) for i in range(0, len(body), 3)]
        elif kind == b"IDAT":
            compressed += body
        pos += 12 + length
    width, height, depth, colour_type, _, _, interlace = header
    if depth != 8 or interlace or colour_type not in CHANNELS:
        raise ValueError("only 8-bit non-interlaced PNG images are supported")

    size = CHANNELS[colour_type]
    image = []
    for line in unfilter(zlib.decompress(compressed), width, height, size):
        pixels = [line[i:i + size] for i in range(0, len(line), size)]
        if colour_type == 3:
            image.append([palette[p[0]] for p in pixels])
        elif colour_type in (0, 4):
            image.append([(p[0],) * 3 for p in pixels])
        else:
            image.append([tuple(p[:3]) for p in pixels])
    return image


def roll(stack):
    rolls, depth = stack.pop(), stack.pop()
    if depth <= 0 or depth > len(stack):
        return
    section = stack[-depth:]
    rolls %= depth
    stack[-depth:] = section[-rolls:] + section[:-rolls] if rolls else section


def run_piet(data):
    image = read_png(data)
    height, width = len(image), len(image[0])
    # Colours outside the Piet palette are treated as white
    grid = [[px if px in COLOURS or px == BLACK else WHITE for px in row] for row in image]

    def inside(x, y):
        return 0 <= x < width and 0 <= y < height and grid[y][x] != BLACK

    def block(x, y):
        colour, seen, todo = grid[y][x], {(x, y)}, [(x, y)]
        while todo:
            cx, cy = todo.pop()
            for dx, dy in DIRECTIONS:
                nxt = (cx + dx, cy + dy)
                if inside(*nxt) and nxt not in seen and grid[nxt[1]][nxt[0]] == colour:
                    seen.add(nxt)
                    todo.append(nxt)
        return seen

    def binary(operation):
        if len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            if b == 0 and operation in ("divide", "mod"):
                stack.extend([a, b])
            else:
                stack.append({
                    "add": a + b, "subtract": a - b, "multiply": a * b,
                    "divide": b and a // b, "mod": b and a % b, "greater": int(a > b),
                }[operation])

    def execute(change, value):
        nonlocal dp, cc
        operation = OPERATIONS[change]
        if operation == "push":
            stack.append(value)
        elif operation in ("add", "subtract", "multiply", "divide", "mod", "greater"):
            binary(operation)
        elif operation == "roll":
            if len(stack) >= 2:
                roll(stack)
        elif operation == "in_number":
            stack.append(read_number())
        elif operation == "in_char":
            stack.append(read_char())
        elif stack:
            top = stack.pop()
            if operation == "not":
                stack.append(int(top == 0))
            elif operation == "pointer":
                dp = (dp + top) % 4
            elif operation == "switch":
                cc = (cc + top) % 2
            elif operation == "duplicate":
                stack.extend([top, top])
            elif operation == "out_number":
                out(str(top))
            elif operation == "out_char":
                out(chr(top))

    stack, x, y, dp, cc, attempts = [], 0, 0, 0, 0, 0
    while attempts < 8:
        cells = block(x, y)
        dx, dy = DIRECTIONS[dp]
        if grid[y][x] == WHITE:
            # Slide straight across white; a wall turns the pointer instead
            if inside(x + dx, y + dy):
                x, y, attempts = x + dx, y + dy, 0
            else:
                cc, dp, attempts = cc ^ 1, (dp + 1) % 4, attempts + 1
            continue
        furthest = max(cx * dx + cy * dy for cx, cy in cells)
        sx, sy = DIRECTIONS[(dp + (1 if cc else 3)) % 4]
        ex, ey = max((c for c in cells if c[0] * dx + c[1] * dy == furthest), key=lambda c: c[0] * sx + c[1] * sy)
        nx, ny = ex + dx, ey + dy
        if not inside(nx, ny):
            if attempts % 2 == 0:
                cc ^= 1
            else:
                dp = (dp + 1) % 4
            attempts += 1
            continue
        attempts = 0
        if grid[ny][nx] != WHITE:
            (hue, light), (new_hue, new_light) = COLOURS[grid[y][x]], COLOURS[grid[ny][nx]]
            execute(((new_hue - hue) % 6, (new_light - light) % 3), len(cells))
        x, y = nx, ny


# (hue change, lightness change) -> command
OPERATIONS = {
    (0, 1): "push", (0, 2): "pop",
    (1, 0): "add", (1, 1): "subtract", (1, 2): "multiply",
    (2, 0): "divide", (2, 1): "mod", (2, 2): "not",
    (3, 0): "greater", (3, 1): "pointer", (3, 2): "switch",
    (4, 0): "duplicate", (4, 1): "roll", (4, 2): "in_number",
    (5, 0): "in_char", (5, 1): "out_number", (5, 2): "out_char",
}
