# Python - Async

This repository contains a series of Python asynchronous functions and coroutines.

## Table of Contents

1. [The Basics of Async](#the-basics-of-async)
2. [Let's Execute Multiple Coroutines at the Same Time with Async](#lets-execute-multiple-coroutines-at-the-same-time-with-async)
3. [Measure the Runtime](#measure-the-runtime)
4. [Tasks](#tasks)
5. [Tasks (Task Wait N)](#tasks-task-wait-n)

## The Basics of Async

**File:** [0-basic_async_syntax.py](0-basic_async_syntax.py)

Write an asynchronous coroutine called `wait_random` that takes an integer argument `max_delay` (with a default value of 10).

- **Description:** The coroutine will wait for a random delay between 0 and `max_delay` (inclusive, float value) seconds and eventually return it. Use the `random` module.

## Let's Execute Multiple Coroutines at the Same Time with Async

**File:** [1-concurrent_coroutines.py](1-concurrent_coroutines.py)

Write an async routine called `wait_n` that takes in 2 integer arguments: `n` and `max_delay`.

- **Description:** This routine will spawn `wait_random` `n` times with the specified `max_delay`. `wait_n` should return the list of all the delays (float values) in ascending order without using `sort()` because of concurrency.

## Measure the Runtime

**File:** [2-measure_runtime.py](2-measure_runtime.py)

Create a function `measure_time` with integers `n` and `max_delay` as arguments.

- **Description:** This function will measure the total execution time for `wait_n(n, max_delay)`, and return `total_time / n`. Your function should return a float. Use the `time` module to measure an approximate elapsed time.

## Tasks

**File:** [3-tasks.py](3-tasks.py)

Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

- **Description:** Import `wait_random` from `0-basic_async_syntax`. Do not create an async function; use regular function syntax.

## Tasks (Task Wait N)

**File:** [4-tasks.py](4-tasks.py)

Alter the `wait_n` code to create a new function `task_wait_n`.

- **Description:** The code will be nearly identical to `wait_n` except `task_wait_random` is called instead.

Feel free to customize it as needed! 😊
