# -*- coding: utf-8 -*-

from contextlib import asynccontextmanager


async def download_webpage(url):
    print(f"downloading:{url}")


async def update_stats(url):
    print(f"update:{url}")


def process(data):
    print(f"processing:{data}")


@asynccontextmanager
async def web_page(url):
    data = await download_webpage(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)
