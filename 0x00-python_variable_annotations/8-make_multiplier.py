#!/usr/bin/env python3

"""
Module: 8-make_multiplier
Description: Contains a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: The multiplier function.
    """
    def multiplier_func(number: float) -> float:
        """
        Multiplies a number by the multiplier value.

        Args:
            number (float): The number to multiply.

        Returns:
            float: The multiplied result.
        """
        return number * multiplier

    return multiplier_func
