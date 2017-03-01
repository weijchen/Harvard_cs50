# encoding: utf-8

# set the initial status of the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# set the function's variables by type directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# set the function's variables by two-step
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# variables' value can type in mathematical method
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# combine 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
