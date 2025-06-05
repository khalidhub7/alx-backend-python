#!/usr/bin/env python3
""" simple async chatbot interaction """

import asyncio
from typing import AsyncGenerator


async def chat() -> AsyncGenerator[str, str]:
    """ async chat generator """

    name = yield 'your name?'
    age = yield 'your age?'

    yield f"Welcome {name}, {age} years old 😇"


async def main():
    """ test """

    newchat = chat()

    await newchat.__anext__()  # this mean start the chatbot

    await newchat.asend('khalid')
    result = await newchat.asend('22')

    print(result)

asyncio.run(main())
