# -*- coding: utf-8 -*-

import asyncio, time

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} GoodBye!")

asyncio.run(main())