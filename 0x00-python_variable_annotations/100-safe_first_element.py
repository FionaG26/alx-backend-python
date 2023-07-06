#!/usr/bin/env python3

"""
Module: 100-safe_first_element
Description: Contains a function to retrieve
the first element of a sequence safely.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence safely.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
