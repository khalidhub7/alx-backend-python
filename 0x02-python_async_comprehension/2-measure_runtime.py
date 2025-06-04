#!/usr/bin/env python3
""" python async comprehension """

import asyncio
import time
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run time for four parallel comprehensions """

    coroutines = [
        async_comprehension()
        for _ in range(4)
    ]

    start = asyncio.get_event_loop().time()

    await asyncio.gather(*coroutines)

    end = asyncio.get_event_loop().time()

    return end - start
