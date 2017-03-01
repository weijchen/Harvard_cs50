# -*- coding: utf-8 -*-
# PN: 
# Version 1.0
# KW: requests.get(), find name
# ---------------------------------------------------

import requests




url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的名字 ")
html = requests.get(url).text
if name in html:
	print("yes")
else:
	print("no")