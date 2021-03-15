#!/usr/bin/env python3
"""Task requires us to add annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
	""""
	--------------------------
	METHOD: safe_first_element
	--------------------------
	Description:
		Returns the first element in any
		iterable datatype
	"""
	if lst:
		return lst[0]
	else:
		return None
