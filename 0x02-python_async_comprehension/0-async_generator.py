#!/usr/bin/env python3
"""module implements an asynchronous routine"""

from random import uniform
from typing import Generator
import asyncio


async def async_generator() -> Generator[int, None, None]:
    """
    that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    :return: Generator[int, None, None]
    """
    rand_num = uniform(0, 10)  # generates a rnd floating int
    for _ in range(10):
        await asyncio.sleep(1)  # waits synchronously for a sec
        yield rand_num
