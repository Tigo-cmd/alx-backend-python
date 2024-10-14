#!/usr/bin/env python3
"""module implements an asynchronous routine"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()  # Record the start time

    # Run the wait_n coroutine and wait for completion
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate total elapsed time

    # Return the average time per coroutine
    return total_time / n
