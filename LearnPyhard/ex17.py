# encoding: utf-8

from sys import argv
# return TRUE if a file exists,
# based on file's name in a string as an argument
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# capture content from 'from_file'
in_file = open(from_file)
indata = in_file.read()

# calculate content size of from_file
print "The input file is %d bytes long" % len(indata)

# use exsits command to test file's exsistence
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
# make a new line, same function as \n
raw_input()
# paste from_file's content to to_file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
