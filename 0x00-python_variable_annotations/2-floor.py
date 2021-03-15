#!/usr/bin/env python3
"Floor Function"


def floor(n: float) -> int:
    """
    --------------
    METHOD: floor
    --------------
    Description:
            Method that returns an int value from
            a float stored in @n:
    """
    return int(n) if n >= 0 else int(n) - 1
