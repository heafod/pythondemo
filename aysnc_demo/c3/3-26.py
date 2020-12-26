# -*- coding: utf-8 -*-

import asyncio
from aioredis import create_redis

async def do_something_with(value):
    print(value)

async def main():
    redis = await create_redis(('localhost', 6379), password='passw0rd')
    keys = ['Americas', 'Africa', 'Europe', 'Asia']

    async for value in one_at_a_time(redis, keys):
        await do_something_with(value)

async def one_at_a_time(redis, keys):
    for k in keys:
        value = await redis.get(k)
        yield value

asyncio.run(main())
