# encoding: utf-8

from sys import argv

script, filename = argv

print ("you are opening %r") % filename
print ("> ")
open_file = open(filename)
print open_file.read()
