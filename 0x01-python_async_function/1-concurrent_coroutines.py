#!/usr/bin/env python3
"""module implements an asynchronous routine"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        if len(delays) == 0 or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break

    return delays
