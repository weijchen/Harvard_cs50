# encoding: utf-8

# like the scripts with argv
# tell Python we want to make a new function 'print_two'
# * tells Python to take all the arguments to the function
# and put in relative argument
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args is actually pointless
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# with one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# with no argumnets
def print_none():
    print "I got nothin'."

print_two("Jimmy", "Chen")
print_two_again("Jimmy", "Chen")
print_one("Jimmy")
print_none()
