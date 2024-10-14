#!/usr/bin/env python3
""" basics of async """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """ measure time """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    sum = (end - start) / n
    return sum
