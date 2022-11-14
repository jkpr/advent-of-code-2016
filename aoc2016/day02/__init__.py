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


def bounded(x: int, y: int):
    if x < -1:
        x = -1
    elif x > 1:
        x = 1
    if y < -1:
        y = -1
    elif y > 1:
        y = 1
    return x, y


def move(current: tuple[int, int], command: str) -> tuple[int, int]:
    if command == "U":
        delta = (0, 1)
    elif command == "D":
        delta = (0, -1)
    elif command == "L":
        delta = (-1, 0)
    elif command == "R":
        delta = (1, 0)
    else:
        raise NotImplementedError()
    new_pos = bounded(current[0] + delta[0], current[1] + delta[1])
    return new_pos


def translate_to_number(current: tuple[int, int]) -> str:
    x = current[0]
    y = current[1]
    number = (x + 1) + (2 - (y + 1)) * 3 + 1
    return str(number)


def part1(lines: list[str]):
    code = []
    current = (0, 0)
    for line in lines:
        for command in line:
            current = move(current, command)
        code.append(translate_to_number(current))
    return "".join(code)

POS_TO_CODE = {
    (0, 2): "1",
    (-1, 1): "2",
    (0, 1): "3",
    (1, 1): "4",
    (-2, 0): "5",
    (-1, 0): "6",
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, -1): "A",
    (0, -1): "B",
    (1, -1): "C",
    (0, -2): "D",
}


def move2(current: tuple[int, int], command: str) -> tuple[int, int]:
    if command == "U":
        delta = (0, 1)
    elif command == "D":
        delta = (0, -1)
    elif command == "L":
        delta = (-1, 0)
    elif command == "R":
        delta = (1, 0)
    else:
        raise NotImplementedError()
    new_pos = (current[0] + delta[0], current[1] + delta[1])
    if new_pos in POS_TO_CODE:
        return new_pos
    return current


def part2(lines: list[str]):
    code = []
    current = (-2, 0)
    for line in lines:
        for command in line:
            current = move2(current, command)
        code.append(POS_TO_CODE[current])
    return "".join(code)
