#!/usr/bin/env python3
""" basic annotations """
from typing import Sequence, Any, Union

# The types of the elements of the input are not know
# OK, let’s make it known


def safe_first_element(lst: Sequence[Any]
                       ) -> Union[Any, None]:
    """ duck typing first element as sequence """
    if lst:
        return lst[0]
    else:
        return None
