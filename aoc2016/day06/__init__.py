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
    most = []
    for col in zip(*lines):
        c = Counter(col)
        most.append(c.most_common(1)[0][0])
    return ''.join(most)


def part2(lines: list[str]):
    least = []
    for col in zip(*lines):
        c = Counter(col)
        least.append(c.most_common()[-1][0])
    return ''.join(least)
