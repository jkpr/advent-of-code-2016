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


def part1(lines: list[str]):
    valid = 0
    for line in lines:
        a, b, c = sorted(int(i) for i in line.split())
        if a + b > c:
            valid += 1
    return valid


def part2(lines: list[str]):
    valid = 0
    data = []
    for line in lines:
        data.append([int(i) for i in line.split()])
    transverse = list(zip(*data))
    for col in transverse:
        for i in range(len(col) // 3):
            a, b, c = sorted(col[(3*i):(3*i+3)])
            if a + b > c:
                valid += 1
    return valid
