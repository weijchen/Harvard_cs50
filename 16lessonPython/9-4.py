# -*- coding: utf-8 -*-
# PN: Email finder
# Version 1.0
# KW: email, find, regex, findall
# ---------------------------------------------------

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+)"
url = 'http://www.taifex.com.tw/chinese/2/TFO.asp'

html = requests.get(url).text

emails = re.findall(regex, html)
for email in emails:
	print(email)