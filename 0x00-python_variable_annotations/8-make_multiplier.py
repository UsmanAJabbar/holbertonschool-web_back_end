#!/usr/bin/env python3
"""Make multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    -----------------------
    METHOD: make_multiplier
    -----------------------
    Description:
            Takes in an argument and returns a function
            that multiplies a float by @multiplier.
    """
    return lambda x: multiplier * x
