#!/usr/bin/env python3
""" async comprehension """
from typing import List
async_gen = __import__(
    '0-async_generator').async_generator


async def async_comprehension(
) -> List[float]:
    """ async for """
    return [i async for i in async_gen()]
