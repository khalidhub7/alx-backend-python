#!/usr/bin/env python3
"""generic utilities for github org client."""

import requests
from functools import wraps
from typing import (Mapping, Sequence, Any,
                    Dict, Callable)

__all__ = [
    "access_nested_map",
    "get_json", "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """access nested map with key path

    parameters
    ----------
    nested_map : mapping
        a nested dictionary
    path : sequence
        a sequence of keys representing the path
    example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
            """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """get json from remote url"""
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """decorator to memoize a method.
    example
    -------
    class myclass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> obj = myclass()
    >>> obj.a_method
    a_method called
    42
    >>> obj.a_method
    42
            """

    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """memoized wrapper"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
