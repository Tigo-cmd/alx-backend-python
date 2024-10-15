#!/usr/bin/env python3
"""module implements an asynchronous routine"""

from random import uniform
from typing import Generator
import asyncio


async def async_generator() -> Generator[int, None, None]:
    rand_num = uniform(0.0, 10)
    for _ in range(10):
        await asyncio.sleep(1)
        yield rand_num
