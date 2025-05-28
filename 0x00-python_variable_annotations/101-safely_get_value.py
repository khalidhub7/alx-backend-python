#!/usr/bin/env python3
""" basic annotations """
from typing import Any, Union, TypeVar, Mapping
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None
                     ) -> Union[Any, T]:
    """ get dict value safely """
    if key in dct:
        return dct[key]
    else:
        return default
