# encoding: utf-8
# PN: Earthquake
# Version 1.0
# key word: json, datatime, .format function fetching tags, datetime process
# -------------------------------------------------------------
import json, datetime

fp = open('data.json', 'r')
earthquake = json.load(fp)

print("過去7天全球發生重大的地震資訊: ")
for eq in earthquake['features']:
	print("地點:{}".format(eq['properties']['place']))
	print("震度:{}".format(eq['properties']['mag']))
	et = float(eq['properties']['time'])/1000
	d = datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
	print("時間:{}".format(d))