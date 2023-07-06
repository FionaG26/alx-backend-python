#!/usr/bin/env python3

"""
Module: 6-sum_mixed_list
Description: Contains a function to calculate the sum of a list
of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(
        mxd_lst: List[Union[int, float]]
) -> float:
    """
    Calculates the sum of a list of integers and floats and returns
    the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]):
            The list of integers and floats.

    Returns:
        float: The sum of the integers and floats.
    """
    return sum(mxd_lst)
