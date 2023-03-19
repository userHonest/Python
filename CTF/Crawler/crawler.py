#!/usr/bin/env python

import argparse
import requests
import re
from urllib.parse import urlparse, urljoin

# Commandline Arguments
parser = argparse.ArgumentParser()
parser.add_argument('url', help='the URL to crawl')
args = parser.parse_args()

target_url = args.url
target_links = []


# this code extracts links from a webpage using regular expressions
def extract_links(url):
    response = requests.get(url)
    try:
        content = response.content.decode('utf-8')
    except UnicodeDecodeError:
        return []
    return re.findall('(?:href=")(.*?)"', content)


# Takes a single argument url
def crawl(url):
    href_links = extract_links(url)

    for link in href_links:
        link = urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


# launch program
crawl(target_url)
