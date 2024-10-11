#!/usr/bin/env python3
"""annotates a given function parameters and return with appropriate types"""
from typing import Iterable, Union, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns the length for a given item in a lst
    :param lst:  to be iterated
    :return: item and list
    """
    return [(i, len(i)) for i in lst]
