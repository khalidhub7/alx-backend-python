#!/usr/bin/env python3
""" basic annotations """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]
          ) -> Tuple[str, float]:
    """ return key and value squared """
    return (k, float(v * v))
