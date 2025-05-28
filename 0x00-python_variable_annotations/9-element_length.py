#!/usr/bin/env python3
""" basic annotations """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """ pair each element with its len """
    return [(i, len(i)) for i in lst]
