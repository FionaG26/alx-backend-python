#!/usr/bin/env python3

"""
Module: 7-to_kv
Description: Contains a function to convert
a string and an int/float to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and an int/float to a tuple.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float.

    Returns:
        Tuple[str, float]: The resulting tuple.
    """
    return (k, v ** 2)
