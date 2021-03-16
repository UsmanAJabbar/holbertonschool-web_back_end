#!/usr/bin/env python3
"""Measures runtime"""

async def measure_time(n: int, max_delay: int) -> float:
	"""
	--------------------
	METHOD: measure_time
	--------------------
	Description:
		Returns in float how long it took to
		execute and return from the wait_n
		function
	Args:
		Notes -> n and max_delay are to be passed
		to the wait_n function

	    @n: runs wait_random n number of times
        @max_delay: specifies the max delay with
        each run of wait_random
	"""
	wait_n = __import__('1-concurrent_coroutines').wait_n
	final = await wait_n(n, max_delay)
	return final
