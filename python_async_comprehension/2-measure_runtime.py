#!/usr/bin/env python3

"""
This module demonstrates measuring the runtime
of asynchronous comprehensions
executed concurrently using asyncio and timeit.

The measure_runtime coroutine measures the total
runtime of four concurrent
calls to the async_comprehension coroutine.
"""

import asyncio
import random
import timeit
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of four concurrent
    async_comprehension coroutines.

    Returns:
        float: The total time taken to run the
        four async_comprehension coroutines.
    """
    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = timeit.default_timer()
    return stop - start
