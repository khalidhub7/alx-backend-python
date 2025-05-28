#!/usr/bin/env python3
""" basic annotations """
from typing import Callable


def make_multiplier(multiplier: float
                    ) -> Callable[[float], float]:
    """ creates multiplier func """
    def fun(x: float) -> float:
        return multiplier * x
    return fun
