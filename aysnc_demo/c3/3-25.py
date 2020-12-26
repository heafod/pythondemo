# -*- coding: utf-8 -*-

import asyncio
from aioredis import create_redis


async def do_something_with(value):
    print(value)


async def main():
    redis = await create_redis(('localhost', 6379), password='passw0rd')
    keys = ['Americas', 'Africa', 'Europe', 'Asia']

    async for value in OneAtAtime(redis, keys):
        await do_something_with(value)


class OneAtAtime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        value = await self.redis.get(k)
        return value

asyncio.run(main())