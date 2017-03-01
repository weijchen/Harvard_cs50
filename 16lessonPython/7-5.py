# encoding: utf-8
# PN: 9 * 9 charts
# version: 1.0

# -------------------------------------------------solution 1
for i in range(1,10,3):
	for j in range(1,10):
		print('%d * %d = %d    ' %(i, j, i*j), end="")
		print('%d * %d = %d    ' %(i+1, j, (i+1)*j), end="")
		print('%d * %d = %d    ' %(i+2, j, (i+2)*j))
	print()
# -------------------------------------------------solution 2
for i in range(1,10,3):
	for j in range(1,10):
		print('{}*{} = {:>2}    ' .format(i, j, i*j), end="")
		print('{}*{} = {:>2}    ' .format(i+1, j, (i+1)*j), end="")
		print('{}*{} = {:>2}    ' .format(i+2, j, (i+2)*j))
	print()