#!/usr/bin/env python3
"Task requires us to add annotations"
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    ----------------------
    METHOD: element_length
    ----------------------
    Description:
            This function returns the
            length of each iterable in @lst
    """
    return [(i, len(i)) for i in lst]
