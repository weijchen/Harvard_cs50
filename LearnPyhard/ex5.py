# encoding: utf-8

my_name = 'Jimmy Chen'
my_age = 24
my_height = 172
my_height_inch = my_height/ 2.54
my_weight = 63
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

# Python format characters %s, %d, %r(no matter what it is, print it!)
print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilograms heavy" % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print my_height_inch
