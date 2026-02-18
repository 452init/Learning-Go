from itertools import zip_longest, chain


def transpose(text) -> str:
    lines = text.splitlines()

    target_widths = []
    current_max = 0
    for line in reversed(lines):
        current_max = max(current_max, len(line))
        target_widths.append(current_max)
    target_widths.reverse()

    # Pad lines to the required width
    padded = [line.ljust(w) for line, w in zip(lines, target_widths)]

    # Transpose and join (like you already do)
    transposed = zip_longest(*padded, fillvalue='')
    return '\n'.join(''.join(row) for row in transposed)