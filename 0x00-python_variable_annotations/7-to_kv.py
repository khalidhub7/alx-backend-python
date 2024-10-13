#!/usr/bin/env python3
""" basic annotations """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ square """
    return (k, float(v ** 2))
