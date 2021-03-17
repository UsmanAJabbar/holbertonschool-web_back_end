#!/usr/bin/env python3
"""Async Generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    -----------------------
    METHOD: async_generator
    -----------------------
    Description:
        Generates and returns a float
        n number of times to an async
        generator call in main()
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
