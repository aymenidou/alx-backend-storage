#!/usr/bin/env python3
'''0x02-redis_basic'''
import redis
import uuid
from typing import Union, Callable, Any
import functools


class Cache:
    '''Cache class '''

    def __init__(self):
        '''initialisation function'''
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush the database on initialization

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a randomly generated key
          and returns the key."""
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key

    def get(self, key: str, fn: Callable = None) -> Any:
        """Retrieves data from Redis by key, optionally applying
          a conversion function."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)  # Apply conversion if a function is provided
        return data

    def get_str(self, key: str) -> str:
        """Retrieves data as a string."""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """Retrieves data as an integer."""
        return self.get(key, fn=int)

    def count_calls(self, method: Callable) -> Callable:
        """
        Decorator that counts calls to a method and returns
          a wrapped function.
        """

        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Get the qualified name of the method
            key = method.__qualname__
            # Increment the call count for the method
            self._redis.incr(key)
            # Call the original method and return its result
            return method(self, *args, **kwargs)

        return wrapper
