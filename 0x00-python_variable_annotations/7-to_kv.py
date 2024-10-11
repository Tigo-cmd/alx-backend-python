#!/usr/bin/env python3
"""this module implements an annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns something to be annotated
    :param k:  a string
    :param v: an int OR float
    :return: returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v
    """
    return k, v ** 2
