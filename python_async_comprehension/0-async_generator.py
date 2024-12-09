#!/usr/bin/env python3

"""
This module demonstrates an asynchronous generator.
The async_generator coroutine yields random numbers
between 0 and 10
with a delay of 1 second between each yield.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This asynchronous generator
    coroutine yields random floating-point
    numbers between 0 and 10.
    It waits for 1 second between yields.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
