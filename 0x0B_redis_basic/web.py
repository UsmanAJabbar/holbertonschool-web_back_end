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
    if type(url) is str and type(exp) is int:
        req = r_get(url)

        if not cache.get(f"count:{url}"):
            cache.set(f"count:{url}", 1, exp)
        else:
            cache.incr(f"count:{url}")

        return req.text

# get_page('http://slowwly.robertomurray.co.uk')
# get_page('http://slowwly.robertomurray.co.uk')
# get_page('https://usmanjabbar.com')
# get_page()
# print(cache.get(f"count:http://slowwly.robertomurray.co.uk"))
# print(cache.get(f"count:https://usmanjabbar.com"))
