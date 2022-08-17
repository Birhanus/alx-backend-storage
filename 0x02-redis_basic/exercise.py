#!/usr/bin/env python3
"""Writing stringa to Redis"""
from uuid import uuid4
import redis


class Cache:
    """A Cache class"""
    def __init__(self) -> None:
        """store an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data argument and retuns a string .
        The method should generate a random key(eg using uuid)
        and store the input data in Redis using the random key
        and return the kety"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
