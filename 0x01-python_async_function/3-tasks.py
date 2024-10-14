#!/usr/bin/env python3
""" basics of async """
import asyncio
wait_ran = __import__('prev').wait_random


def task_wait_random(max_delay):
    """ task """
    return asyncio.create_task(wait_ran(max_delay))
