#!/usr/bin/env python3
""" basic annotations """
from typing import Callable


def make_multiplier(multiplier: float
                    ) -> Callable[[float], float]:
    """ multiplier """
    return lambda x: x * multiplier
