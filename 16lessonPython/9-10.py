# -*- coding: utf-8 -*-
# PN: data output web-style
# Version 1.0
# KW: local server
# --------------------------------------------------- libs import
from bs4 import BeautifulSoup as bs
import requests
import sys, os
from urllib.parse import ulrparse
from urllib.request import ulropen
# --------------------------------------------------- html part
if len(sys.argv) < 2:
	print("用法: python 9-10.py <<target url>>")
	exit(1)

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)    # find web domain name
html = requests.get(url).text
sp = bs(html, "html.parser")
# --------------------------------------------------- html part

pre_html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>網頁搜集來的資料</title>
	<meta name="viewpoint" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></script>
	<style>
	.carousel-inner > .item > img,
	.carousel-inner > .item > a > ing {
	border: 5px solid white;
	width: 50%;
	box-shadow: 10px 10px 5px #888888;
	margin: auto;
	}
	</style>

</head>
<body>
<center><h3>以下是從網頁搜集而來的圖片跑馬燈</h3></center>
"""



html_body = """
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    <div class="item">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    ...
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
"""

"""
</head>
<body>
<h2>中油油價歷史資料(取自中油官方網站)</h2>
<table width=600 border=1>
<tr>
	<td>日期</td>
	<td>92無鉛</td>
	<td>95無鉛</td>
	<td>98無鉛</td>
</tr>
"""
post_html = """
</table>
</body>
</html>
"""
# --------------------------------------------------- crawler
all_links = sp.find_all(['a', 'img'])

carousel_part1 = ""
carousel_part2 = ""
picno = 0

for link in all_links:
	src = link.get('src')
	href = link.get('href')
	targets = [src, href]
for t in targets:
	if t != None and ('.jpg' in t or '.png' in t):
		if t.startwith('http'):
			full_path = t
			full_path = domain + t
		else:
			print(full_path)
			image_dir = url.split('/')[-1]
		if not os.pathlexists(image_dir):
			os.mkdir(image_dir)
		filename = full_path.split('/')[-1]
		ext = filename.split('.')[-1]
		filename = full_path.split('/')[-2]
		if ''



prices = list()
for row in rows:
	cols = row.find_all('td')
	if len(cols[1].text) > 0:
		item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
		prices.append(item)

html_body = ""
for p in prices:
	html_body += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(p[0], p[1], p[2], p[3])
html_file = pre_html + html_body + post_html

fp = open('oilprice.html', 'w')
fp.write(html_file)
fp.close
















