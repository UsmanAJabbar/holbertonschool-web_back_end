#!/usr/bin/env python3
"""sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    ----------------
    METHOD: sum_mixed_list
    ----------------
    Description:
        Takes in a list of floats and returns
        the sum of elements as a float
    """
    return sum(mxd_lst)
