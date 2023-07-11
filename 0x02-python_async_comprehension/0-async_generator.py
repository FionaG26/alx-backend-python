#!/usr/bin/env python3
"""
Module: 0-async_generator
-------------------------
This module contains a coroutine called `async_generator`
that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
