#!/usr/bin/env python3

"""
Module: 9-element_length
Description: Contains a function to calculate the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in a list and returns a list of tuples.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples containing an element
        from lst and its length.
    """
    return [(i, len(i)) for i in lst]
