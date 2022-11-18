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


def supports_tls(line: str) -> bool:
    has_abba = False
    in_brackets = False
    for i in range(len(line) - 3):
        substr = line[i:(i+4)]
        if '[' in substr:
            in_brackets = True
            continue
        if ']' in substr:
            in_brackets = False
            continue
        abba = substr == substr[::-1] and substr[0] != substr[1]
        if in_brackets and abba:
            return False
        elif not in_brackets and abba:
            has_abba = True
    return has_abba


def part1(lines: list[str]):
    count = 0
    for line in lines:
        supports = supports_tls(line)
        if supports:
            print("+", line)
        else:
            print("-", line)
        count += supports_tls(line)
    return count


def window(text: str, size: int):
    i = 0
    while i + size <= len(text):
        yield text[i:(i+size)]
        i += 1


def chunkify(text: str):
    supernet = []
    hypernet = []
    in_brackets = False
    while True:
        if not in_brackets:
            next_start = text.find("[")
            if next_start < 0:
                supernet.append(text)
                break
            else:
                supernet.append(text[:next_start])
            in_brackets = True
            text = text[(next_start + 1):]
        else:
            next_end = text.find("]")
            if next_end < 0:
                hypernet.append(text)
                break
            else:
                hypernet.append(text[:next_end])
            in_brackets = False
            text = text[(next_end + 1):]
    return supernet, hypernet


def get_aba(net_items: list[str]) -> set[str]:
    aba = set()
    for item in net_items:
        for chunk in window(item, 3):
            if chunk == chunk[::-1] and chunk[0] != chunk[1]:
                aba.add(chunk)
    return aba


def part2(lines: list[str]):
    count = 0
    for line in lines:
        supernet, hypernet = chunkify(line)
        supernet_aba = get_aba(supernet)
        hypernet_aba = get_aba(hypernet)
        inverted_hypernet_aba = {a[1] + a[0] + a[1] for a in hypernet_aba}
        if supernet_aba & inverted_hypernet_aba:
            count += 1
    return count
