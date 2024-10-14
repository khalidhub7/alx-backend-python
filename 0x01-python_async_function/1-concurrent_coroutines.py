#!/usr/bin/env python3
""" basics of async """
import asyncio
wait_ran = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ multiplee coroutines """
    tasks = []
    for i in range(n):
        tasks.append(wait_ran(max_delay))
    all = asyncio.as_completed(tasks)  # sort tasks
    finished = []
    for j in all:
        result = await j
        finished.append(result)
    return finished
