#!/usr/bin/env python3
""" Redis Cache File """
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
    -----------------------
    METHOD: count_decorator
    -----------------------
    Description:
        Decorator that counts the number of
        times a method was called.
    Args:
        @fn: method to count
    """
    key = fn.__qualname__

    @wraps(fn)
    def call_counter(self, *args, **kwargs):
        self._redis.incr(key)
        return fn(self, *args, **kwargs)

    return call_counter


class Cache:
    """ Redis Caching class """

    def __init__(self):
        """ Initializes the Cache object with a redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds data to the redis database """
        if data:
            from uuid import uuid4
            key = str(uuid4())
            value = data
            self._redis.set(key, data)
            return key or ''

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Given a key, fetches data from the redis client """
        data = self._redis.get(key)
        return data if not fn else fn(data)
