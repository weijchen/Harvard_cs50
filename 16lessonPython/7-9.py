# encoding: utf-8
# PN: Iterator, map()
# version: 1.0


def pick(x):
	fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
	return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
# map("執行用函數","容器變數")
choices = map(pick, alist)
for choice in choices:
	print(choice)