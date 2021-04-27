#!/usr/bin/env python3
""" Redis Cache File """
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps


def replay(obj: Union[Callable, str]) -> None:
    """ Returns a printed history of inputs and outputs """
    cache = obj.__self__

    call_count = str(cache.get(cache.store.__qualname__), 'UTF-8')
    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print(f'{obj.__qualname__} was called {call_count} times:')

    for input, output in zip(inputs, outputs):
        input, output = str(input, 'UTF-8'), str(output, 'UTF-8')
        print(f'{obj.__qualname__}(*{input}) -> {output}')


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


def call_history(fn: Callable) -> Callable:
    """
    --------------------
    METHOD: call_history
    --------------------
    Description:
        Keeps a history the inputs and outputs
    """
    key = fn.__qualname__

    @wraps(fn)
    def history_dec(self, *args, **kwargs):
        self._redis.rpush(f'{key}:inputs', str(args))
        data = fn(self, *args, *kwargs)
        self._redis.rpush(f'{key}:outputs', data)
        return data

    return history_dec


class Cache:
    """ Redis Caching class """

    def __init__(self):
        """ Initializes the Cache object with a redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds data to the redis database """
        if data:
            from uuid import uuid4
            key = str(uuid4())
            value = data
            self._redis.set(key, data)
            return key or ''

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Given a key, fetches data from the redis client """
        data = self._redis.get(key)
        return data if not callable(fn) else fn(data)
