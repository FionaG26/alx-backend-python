#!/usr/bin/env python3

"""
Module: 101-safely_get_value
Description: Contains a function to safely retrieve a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value for.
        default (Union[T, None], optional): The
        default value if the key is not present.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key
        if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
