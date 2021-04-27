#!/usr/bin/env python3
""" Adv task webs module """
from requests import get as r_get
from typing import Callable
from redis import Redis
cache = Redis()
cache.flushdb()


def get_page(url: str = 'http://slowwly.robertomurray.co.uk') -> None:
    """ Runs a GET request on a given URL """
    req = r_get(url)

    if not cache.get(f"count:{url}"):
        cache.set(f"count:{url}", 1, 10)
    else:
        cache.incr(f"count:{url}")

# get_page()
# get_page()
# get_page()
# get_page()
# print(cache.get(f"count:http://slowwly.robertomurray.co.uk"))
