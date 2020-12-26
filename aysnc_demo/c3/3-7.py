# -*- coding: utf-8 -*-
import asyncio

async def f():
    await asyncio.sleep(1.0)
    return 123

async def main():
    result = await f()
    return result

