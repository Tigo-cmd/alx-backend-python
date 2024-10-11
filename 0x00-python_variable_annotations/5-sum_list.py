#!/usr/bin/env python3
"""this implements a type annotated function"""


def sum_list(input_list: list[float]) -> float:
    """
    takes an input list of floats and returns the sum of the floats
    :param input_list: list of floats to be inputted
    :return: sum of floats
    """
    # sumlist: int = 0
    # for i in input_list:
    #     sumlist += i
    # return sumlist     ...this works fine but i just want an error free implelmentation

    return sum(input_list)
