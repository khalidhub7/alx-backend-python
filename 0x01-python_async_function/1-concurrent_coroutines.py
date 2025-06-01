#!/usr/bin/env python3
""" basics of async """

import asyncio
from typing import List
wait_random = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int
                 ) -> list[float]:
    """ run wait_random n times concurrently """

    return await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )
