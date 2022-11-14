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
    commands = lines[0].split(", ")
    direction = 0
    point = [0, 0]
    for command in commands:
        delta = command[0]
        if delta == "R":
            direction += 90
            direction %= 360
        elif delta == "L":
            direction -= 90
            direction %= 360
        else:
            raise NotImplementedError()
        distance = int(command[1:])
        if direction == 0:
            point[1] = point[1] + distance
        elif direction == 90:
            point[0] = point[0] + distance
        elif direction == 180:
            point[1] = point[1] - distance
        elif direction == 270:
            point[0] = point[0] - distance
        else:
            raise NotImplementedError()
    return abs(point[0]) + abs(point[1])


def rotate(heading: int, instruction: str):
    if instruction == "R":
        heading += 90
        heading %= 360
    elif instruction == "L":
        heading -= 90
        heading %= 360
    return heading


def move(current: tuple[int, int], heading: int) -> tuple[int, int]:
    if heading == 0:
        delta = (0, 1)
    elif heading == 90:
        delta = (1, 0)
    elif heading == 180:
        delta = (0, -1)
    elif heading == 270:
        delta = (-1, 0)
    else:
        raise NotImplementedError()
    return (current[0] + delta[0], current[1] + delta[1])


def part2(lines: list[str]):
    current = (0, 0)
    heading = 0
    been = set()
    been.add(current)
    commands = lines[0].split(", ")
    for command in commands:
        instruction = command[0]
        heading = rotate(heading, instruction)
        for i in range(int(command[1:])):
            current = move(current, heading)
            if current in been:
                return abs(current[0]) + abs(current[1])
            been.add(current)
