#!/usr/bin/env python3
"""module implements an asychronous routine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
     asynchronous coroutine that takes in an integer argument
     (max_delay, with a default value of 10) named wait_random
     that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    :param max_delay: random choice range
    :return:
    """
    rand_num = random.uniform(0.0, 10)
    await asyncio.sleep(rand_num)
    return rand_num
