#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay (included) and eventually returns it.

    Args:
        max_delay (int): The maximum delay value (default is 10).

    Returns:
        float: The random delay.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
