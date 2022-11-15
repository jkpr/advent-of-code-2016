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


def room_is_real(line: str) -> bool:
    bracket = line.find("[")
    code = line[:bracket]
    counter = Counter(a for a in code if a.isalpha())
    inverse = {}
    for k, v in counter.items():
        current = inverse.get(v, list())
        current.append(k)
        inverse[v] = sorted(current)
    result = []
    for i in range(max(inverse), 0, -1):
        result.extend(inverse.get(i, list()))
    key = ''.join(result[:5])
    checksum = line[(bracket + 1):(bracket + 6)]
    return key == checksum



def parse_score(line: str) -> int:
    if match := search(r"\d+", line):
        return int(match[0])
    return 0


def part1(lines: list[str]):
    score = 0
    for line in lines:
        if room_is_real(line):
            score += parse_score(line)
    return score


def shift(a: str, amount: int) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = letters.find(a)
    new_index = (index + amount) % len(letters)
    return letters[new_index]




def decrypt(line: str):
    score = parse_score(line)
    bracket = line.find("[")
    code = line[:bracket]
    sentence = []
    for a in code:
        if a.isalpha():
            sentence.append(shift(a, score))
        else:
            sentence.append(a)
    return ''.join(sentence)


def part2(lines: list[str]):
    for line in lines:
        if room_is_real(line):
            decrypted = decrypt(line)
            if 'north' in decrypted:
                return parse_score(line)
