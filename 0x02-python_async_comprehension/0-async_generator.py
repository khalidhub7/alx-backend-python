#!/usr/bin/env python3
""" async comprehension """
import asyncio
import random
from typing import Generator


async def async_generator(
) -> Generator[float, None, None]:
    """ arg1: Yield (float)
        arg2: Send (None)
        arg3: Return (None) """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
