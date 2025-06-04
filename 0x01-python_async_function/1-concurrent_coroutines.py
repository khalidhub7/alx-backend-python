#!/usr/bin/env python3
""" basics of async """

import asyncio
from typing import List
wait_random = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int
                 ) -> List[float]:
    """ run wait_random n times concurrently """

    tasks = [
        wait_random(max_delay)
        for _ in range(n)
    ]
    # print(tasks[0]) # real coroutine

    """
    finished = [
        await task
        for task in asyncio.as_completed(tasks)
    ]
    """

    finished = []
    for task in asyncio.as_completed(tasks):
        # print(task) # watcher coroutine
        result = await task  # get result from watcher
        finished.append(result)

    return finished
