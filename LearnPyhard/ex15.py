# encoding: utf-8

from sys import argv

# input two argument in terminal
scripy, filename = argv

# open() use to open a file then set to a variable
# get back a file
txt = open(filename)

print "Here's your file %r" % filename
# command on file, to read file's content
print txt.read()

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)


print txt_again.read()

filename.close()
