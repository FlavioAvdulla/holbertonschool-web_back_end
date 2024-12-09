# Python - Async Comprehension

This repository contains a series of Python coroutines for asynchronous comprehension tasks.

## Table of Contents

1. [Async Generator](#async-generator)
2. [Async Comprehensions](#async-comprehensions)
3. [Run Time for Four Parallel Comprehensions](#run-time-for-four-parallel-comprehensions)

## Async Generator

**File:** [0-async_generator.py](0-async_generator.py)

Write a coroutine called `async_generator` that takes no arguments.

- **Description:** The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

## Async Comprehensions

**File:** [1-async_comprehension.py](1-async_comprehension.py)

Write a coroutine called `async_comprehension` that takes no arguments.

- **Description:** The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

## Run Time for Four Parallel Comprehensions

**File:** [2-measure_runtime.py](2-measure_runtime.py)

Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`.

- **Description:** `measure_runtime` should measure the total runtime and return it. Notice that the total runtime is roughly 10 seconds.

Feel free to customize it as per your needs! 😊
