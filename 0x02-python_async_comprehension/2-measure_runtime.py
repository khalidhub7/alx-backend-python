#!/usr/bin/env python3
""" async comprehension """
import time
import asyncio
async_compr = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime(
) -> float:
    """
- gather(): Waits for all tasks,
    returns results in the given order
- as_completed(): Returns results,
    as soon as each task finishes """
    start = time.time()
    await asyncio.gather(*(
        async_compr(
        ) for _ in range(4)))
    end = time.time()
    return end - start
