#!/usr/bin/env python3
"""Multiple coroutines"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    --------------
    METHOD: wait_n
    --------------
    Description:
        Executes multiple coroutines at
        the same time with async
    Args:
        @n: runs wait_random n number of times
        @max_delay: specifies the max delay with
        each run of wait_random
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    delay_list = [wait_random(max_delay) for i in range(n)]
    completed_tasks = []

    for task in asyncio.as_completed(delay_list):
        completed_tasks.append(await task)

    return completed_tasks
