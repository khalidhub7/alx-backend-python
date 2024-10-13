#!/usr/bin/env python3
""" basic annotations """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum """
    sum: float = 0.00
    for i in input_list:
        sum += i
    return sum
