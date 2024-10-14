#!/usr/bin/env python3
"""module implements an asynchronous routine"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that waits for a random delay.

    :param max_delay: Maximum number of seconds for the delay
    :return: An asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
