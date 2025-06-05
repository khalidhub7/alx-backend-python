#!/usr/bin/env python3
""" simple async chatbot interaction """

import asyncio
from typing import AsyncGenerator


async def chat() -> AsyncGenerator[str, str]:
    """ async chat generator """
    name = yield 'your name?'
    age = yield 'your age?'
    yield f"hi {name}, {age} yrs old 😇"


async def main():
    chatbot = chat()  # paused, waiting for asend()

    ques1 = await chatbot.asend(None)  # Start the generator
    print(ques1)

    ques2 = await chatbot.asend('khalid')
    print(ques2)

    finalMsg = await chatbot.asend('22')
    print(finalMsg)

asyncio.run(main())
