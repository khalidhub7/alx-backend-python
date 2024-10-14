#!/usr/bin/env python3
""" basics of async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ random """
    gen = random.uniform(0, max_delay)
    await asyncio.sleep(gen)
    return gen


async def task_wait_n(n, max_delay):
    """ multiplee coroutines """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    all = asyncio.as_completed(tasks)  # sort tasks
    finished = []
    for j in all:
        result = await j
        finished.append(result)
    return finished
