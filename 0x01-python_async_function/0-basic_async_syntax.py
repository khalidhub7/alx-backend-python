#!/usr/bin/env python3
""" basics of async """
import random
import asyncio


async def wait_random(max_delay=10):
    """ random """
    gen = random.uniform(0, max_delay)
    await asyncio.sleep(gen)
    return gen