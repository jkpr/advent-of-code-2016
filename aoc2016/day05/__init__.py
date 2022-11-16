from collections import (
    Counter,
    defaultdict,
    deque,
    namedtuple,
)
from dataclasses import dataclass
from functools import cache
import hashlib
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


def get_hexdigest(start: str, index: int) -> str:
    m = hashlib.md5()
    key = start + str(index)
    m.update(key.encode(encoding="utf-8"))
    return m.hexdigest()


def part1(lines: list[str]):
    password = []
    i = 0
    while True and i < 50_000_000:
        if len(password) >= 8:
            break
        hexdigest = get_hexdigest(lines[0], i)
        if hexdigest.startswith("00000"):
            password.append(hexdigest[5])
        i += 1
    return ''.join(password)


def part2(lines: list[str]):
    password = ['.'] * 8
    i = 0
    while True and i < 50_000_000:
        if "." not in password:
            break
        hexdigest = get_hexdigest(lines[0], i)
        if hexdigest.startswith("00000"):
            index = hexdigest[5]
            if "0" <= index <= "7":
                if password[int(index)] == ".":
                    character = hexdigest[6]
                    password[int(index)] = character
        i += 1
    return ''.join(password)
