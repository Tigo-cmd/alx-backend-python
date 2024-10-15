#!/usr/bin/env python3
"""module implements an asynchronous routine"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
     coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
     measure_runtime should measure the total runtime and return it.
    :return: total runtime
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()

    return end - start
