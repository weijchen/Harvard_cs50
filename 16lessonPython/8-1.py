# encoding: utf-8

fp = open("zop.txt", "r")
zops = fp.readlines()
fp.close()
i = 1
print('The Zen of Python')
for zop in zops:
	print("zen {}: {}".format(i, zen), end="")
	i += 1