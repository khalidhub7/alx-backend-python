#!/usr/bin/env python3
""" python async comprehension """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator(
) -> AsyncGenerator[int, None]:
    """ async Generator """

    for _ in range(11):
        await asyncio.sleep(1)

        yield random.randint(0, 10)
