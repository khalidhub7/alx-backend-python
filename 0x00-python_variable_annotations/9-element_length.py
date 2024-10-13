#!/usr/bin/env python3
""" basic annotations """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """ function annotations """
    return [(i, len(i)) for i in lst]
