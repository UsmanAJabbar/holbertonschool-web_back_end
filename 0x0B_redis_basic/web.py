#!/usr/bin/env python3
""" Adv task webs module """
from requests import get as r_get
from typing import Callable
from redis import Redis
cache = Redis()
cache.flushdb()


def get_page(url: str = 'http://slowwly.robertomurray.co.uk',
             exp: int = 10) -> None:
    """ Runs a GET request on a given URL """
    req = r_get(url)

    if not cache.get(f"count:{url}"):
        cache.set(f"count:{url}", 1, 10)
    else:
        cache.incr(f"count:{url}")

    return req.text

# get_page()
# get_page()
# get_page()
# get_page()
# print(cache.get(f"count:http://slowwly.robertomurray.co.uk"))
