#!/usr/bin/env python3
"""this module implements an annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns something to be annotated
    :param multiplier:  a float
    :return: returns a function that multiplies a float by multiplier.
    """
    def by_multiplier(value: float) -> float:
        """

        :param value: random float
        :return:
        """
        return value * multiplier
    return by_multiplier
