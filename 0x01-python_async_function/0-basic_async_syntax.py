#!/usr/bin/env python3
"""Await function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    --------------------
    METHOD:: wait_random
    --------------------
    Description:
        Sets a temporary halt for a random duration
        between 0s and value set in @max_delay
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
