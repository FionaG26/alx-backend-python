#!/usr/bin/env python3

"""
Module: 5-sum_list
Description: Contains a function to calculate the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats and returns the result as a float.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats.
    """
    return sum(input_list)
