#!/usr/bin/env python3
"""Module that contains an asynchronous comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension.

    Returns:
        List[float]: The 10 random numbers generated.
    """
    return [i async for i in async_generator()]
