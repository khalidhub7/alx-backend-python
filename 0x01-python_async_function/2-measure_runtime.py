#!/usr/bin/env python3
""" basics of async """
import time
import asyncio
wait_n = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int,
                 max_delay: int) -> float:
    """ measure the runtime of async func """
    start = time.time()  # unix epoch (Jan 1, 1970)

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n
