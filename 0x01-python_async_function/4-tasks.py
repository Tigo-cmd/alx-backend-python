#!/usr/bin/env python3
"""module implements an asynchronous routine"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns
    a list of delays in ascending order.

    :param n: Number of tasks to spawn
    :param max_delay: Maximum delay for each task
    :return: List of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
