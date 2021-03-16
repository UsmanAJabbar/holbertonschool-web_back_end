#!/usr/bin/env python3
"""Await function"""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    --------------------
    METHOD:: wait_random
    --------------------
    Description:
        Sets a temporary halt for a random duration
        between 0s and value set in @max_delay
    """

    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
