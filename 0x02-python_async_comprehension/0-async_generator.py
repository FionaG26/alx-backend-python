#!/usr/bin/env python3
"""
Module: 0-async_generator
-------------------------
This module contains a coroutine called `async_generator`
that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async Generator: async_generator
    -------------------------------
    A coroutine that generates random numbers asynchronously.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
