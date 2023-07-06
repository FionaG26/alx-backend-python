#!/usr/bin/env python3

"""
Module: 102-type_checking
Description: Contains a function to zoom in an array by repeating its elements.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in an array by repeating its elements.

    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
