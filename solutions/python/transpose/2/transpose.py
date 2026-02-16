from itertools import zip_longest, chain


def transpose(text) -> str:
    lines = text.splitlines()

    max_len = 0
    padded_lines = []
    for line in reversed(lines):
        max_len = max(max_len, len(line))

        # Handles the trailing through, 1.) using the maximum length to determine the number of spaces to be added to subsequent lines from bottom up.
        padded_lines.append(chain(line.ljust(max_len)))

    lines = list(reversed(padded_lines))
    transposed = zip_longest(*lines, fillvalue='')

    return '\n'.join(''.join(row) for row in transposed)