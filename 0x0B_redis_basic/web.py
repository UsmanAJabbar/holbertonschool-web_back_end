#!/usr/bin/env python3
""" Adv task webs module """
from requests import get as r_get
from typing import Callable
import redis
redis_db = redis.Redis()
redis_db.flushdb()


def get_page(url: str) -> str:
    """ Runs a GET request on a given URL """
    if type(url) is str:
        req = r_get(url)

        if not redis_db.get(f"count:{url}"):
            redis_db.set(f"count:{url}", 1, 10)
        else:
            redis_db.set(f'count:{url}',                          # name
                         int(redis_db.get(f'count:{url}')) + 1,   # value
                         10)                                      # expiry

        return req.text

# get_page('http://slowwly.robertomurray.co.uk')
# get_page('http://slowwly.robertomurray.co.uk')
# get_page('https://usmanjabbar.com')
# print(redis_db.get(f"count:http://slowwly.robertomurray.co.uk"))
# print(redis_db.get(f"count:https://usmanjabbar.com"))
