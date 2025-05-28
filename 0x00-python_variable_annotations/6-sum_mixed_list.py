#!/usr/bin/env python3
""" basic annotations """
from typing import List, Union


def sum_mixed_list(
        mxd_lst: List[Union[int, float]]) -> float:
    """ sum a list of floats and ints """
    return float(sum(mxd_lst))
