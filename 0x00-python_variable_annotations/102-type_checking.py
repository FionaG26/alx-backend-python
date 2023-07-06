#!/usr/bin/env python3

"""
Module: 102-type_checking
Contains the zoom_array function that zooms in an array by a given factor.
"""

from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in the input array by the given factor.

    Args:
        lst: The input array.
        factor: The zoom factor (default is 2).

    Returns:
        The zoomed-in array.
    """
    zoomed_in = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
