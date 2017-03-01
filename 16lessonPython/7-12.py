# encoding: utf-8
# PN: try, except prac
# version: 1.0

while True:
	try:
		age = int(input("What is your age?"))
		break
	except:
		print("Please enter a number")

if age < 15:
	print("You are too")