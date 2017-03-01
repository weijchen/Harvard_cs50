# -*- coding: utf-8 -*-
# PN: 
# Version 1.0
# KW: requests.get(), encoding problems
# ---------------------------------------------------
import requests
url = 'http://udb.moe.edu.tw/Home/About'
html = requests.get(url).text.splitlines()

for i in range(0, 15):
	print(html[i])