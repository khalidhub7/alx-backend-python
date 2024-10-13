#!/usr/bin/env python3
""" basic annotations """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum """
    sum: float = 0.00
    for i in mxd_lst:
        sum += i
    return sum
