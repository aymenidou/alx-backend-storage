#!/usr/bin/env python3
'''0x02-redis_basic'''
import redis
import uuid
from typing import Union


class Cache:
    '''Cache class '''

    def __init__(self):
        '''initialisation function'''
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush the database on initialization

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a randomly generated key
          and returns the key."""
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key
