#!/usr/bin/env python3

import urllib.request
import sys
from bs4 import BeautifulSoup

if len(sys.argv) <= 1:
    print("No URL specified. Please supply a valid http://www.useragentstring.com/ UA list URL")
    sys.exit(1)

ua_url = sys.argv[1]

try:
    with urllib.request.urlopen(ua_url) as f:
        html_doc = f.read()
except Exception as e:
    print(f"Failed to fetch URL: {e}")
    sys.exit(1)

soup = BeautifulSoup(html_doc, 'html.parser')

liste = soup.find(id='liste')

if not liste:
    print("Could not find 'liste' element. Are you on a valid UA list page?")
    sys.exit(1)

uas = liste.find_all('li')

if len(uas) == 0:
    print("No UAs Found. Are you on http://www.useragentstring.com/ lists?")
    sys.exit(1)

for ua in uas:
    ua_string = ua.get_text(strip=True)
    print(ua_string)
