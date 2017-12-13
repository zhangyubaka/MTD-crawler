#!/usr/bin/env python3
# coding=utf-8

import aiohttp
from lxml import etree, html
from pprint import pprint
import asyncio


async def get_page(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            return await resp.text()


async def extract_links(page, xpath: str) -> list:
    root = etree.fromstring(page, etree.HTMLParser())
    links = root.xpath(xpath)
    l = []
    for i in links:
        l.append(i.items()[0][1])
    return l


async def main():
    url = input('Please enter the url for scrapping: ')
    subpages = await extract_links(await get_page(url), xpath='//dd/h3/a[contain(href)]')
    for i in subpages:
        pprint(await extract_links(await get_page(i), xpath='//ul[@id="dl-btn"]//li//a'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
