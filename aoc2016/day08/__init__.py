from collections import (
    Counter,
    defaultdict,
    deque,
    namedtuple,
)
from dataclasses import dataclass
from functools import cache
from itertools import (
    chain,
    combinations,
    groupby,
    permutations,
    product,
    repeat,
)
from math import (
    prod,
    sqrt,
)
from re import (
    search,
    match,
    fullmatch,
    split,
    findall,
    sub,
)

from ..utils import lines_to_int


def rotate(l: list, amount: int) -> list:
    index = amount % len(l)
    if index == 0:
        return list(l)
    return l[-index:] + l[:-index]


def rotate_screen(screen: list[list[str]]) -> list[list[str]]:
    return [list(i) for i in zip(*screen)]


def print_screen(screen):
    for row in screen:
        print(''.join(row))


def part1(lines: list[str]):
    screen = []
    for _ in range(6):
        row = ['.'] * 50
        screen.append(row)
    
    for line in lines:
        found = findall("\d+", line)
        if "rect" in line:
            wide = int(found[0])
            tall = int(found[1])
            for i in range(tall):
                for j in range(wide):
                    screen[i][j] = "#"
        elif "y=" in line:
            row = int(found[0])
            distance = int(found[1])
            rotated = rotate(screen[row], distance)
            screen[row] = rotated
        elif "x=" in line:
            col = int(found[0])
            distance = int(found[1])
            cols = rotate_screen(screen)
            rotated = rotate(cols[col], distance)
            cols[col] = rotated
            screen = rotate_screen(cols)
    count = 0
    for i, row in enumerate(screen):
        for j, pixel in enumerate(row):
            count += pixel == "#"
    
    print_screen(screen)
    
    return count


def part2(lines: list[str]):
    pass
