# -*- coding: utf-8 -*-
# PN: get links contents
# Version 1.0
# KW: bs4, hrefs in website
# ---------------------------------------------------
# --------------------------------------------------- libs import
from bs4 import BeautifulSoup as bs
import requests, sys
# --------------------------------------------------- discription
if len(sys.argv) < 2:
	print("用法: python 9-5.py <<target url>>")
	exit(1)
# --------------------------------------------------- fetch sys second input
url = sys.argv[1]

html = requests.get(url).text
sp = bs(html, 'html.parser')
all_links = sp.find_all('a')

for link in all_links:
	href = link.get('href')
	if href != None and href.startswith('http://'):
		print(href)