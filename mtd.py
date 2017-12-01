#!/usr/bin/env python3
#coding=utf-8

import aiohttp
from lxml import etree, html
from pprint import pprint

async def getPage(url: str):
	async with aiohttp.ClientSession() as session:
		async with session.get(url=url) as resp:
			return await resp.text()

async def extractLinks(page,xpath: str) -> list:
	root = etree.fromstring(page,etree.HTMLParser())
	links = root.xpath(xpath)
	l = []
	for i in links:
		l.append(i.items()[0][1])
	return l

if __name__ == '__main__':
	url = input('Please enter the url for scrapping: ')
	subpages = extractLinks(getPage(url),xpath='//dd/h3/a[contain(href)]')
	links 
	for i in subpages:
		pprint(extractLinks(getPage(i),xpath='//ul[@id="dl-btn"]//li//a'))