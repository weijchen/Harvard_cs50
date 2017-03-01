# encoding: utf-8

# add features to script from the Python feature set
# argv = "argument variable"
from sys import argv

# holds the arguments I pass to my python script on terminal
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
four = raw_input("type a fruit ")
print four

# type three arguments in terminal, will replace first, second, third
