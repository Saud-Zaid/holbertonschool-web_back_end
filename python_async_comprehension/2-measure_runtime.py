#!/usr/bin/env python3
"""Module that measures the total runtime for four parallel comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of four async_comprehensions in parallel.

    Returns:
        float: Total execution time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
