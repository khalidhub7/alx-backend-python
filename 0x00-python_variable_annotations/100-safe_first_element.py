#!/usr/bin/env python3
""" basic annotations """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]
                       ) -> Union[Any, None]:
    """ duck typing """
    if lst:
        return lst[0]
    else:
        return None
