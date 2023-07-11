#!/usr/bin/env python3
"""
Module: 1-async_comprehension
-----------------------------
This module contains a coroutine called `async_comprehension`
that collects 10 random numbers using async comprehension.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
