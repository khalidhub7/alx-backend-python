#!/usr/bin/env python3
""" python async comprehension """

from typing import List
async_generator = __import__(
    '0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async Comprehensions """

    return [
        i async for i in async_generator()
    ]
