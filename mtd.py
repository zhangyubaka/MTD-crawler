#!/usr/bin/env python3
# coding=utf-8

import aiohttp
from lxml import etree
from pprint import pprint
import asyncio
import logging
import coloredlogs

logger = logging.getLogger()
coloredlogs.install(logger=logger)


async def get_page(url: str) -> str:
    logger.info('Getting page...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            logger.debug('Getting ' + url)
            return await resp.text()


async def extract_links(page, xpath: str) -> list:
    logger.info("Extracting links...")
    root = etree.fromstring(page, etree.HTMLParser())
    links = root.xpath(xpath)
    l = []
    for i in links:
        logger.debug("Extracting " + repr(i))
        l.append(i.items()[0][1])
    return l


async def main():
    # url = input('Please enter the url for scrapping: ')
    url = 'http://mac-torrent-download.net/'
    sub_pages = await extract_links(await get_page(url), xpath='//dd/h3/a')
    for i in sub_pages:
        pprint(await extract_links(await get_page(i), xpath='//ul[@id="dl-btn"]//li//a'))


if __name__ == '__main__':
    logger.info('Starting...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
