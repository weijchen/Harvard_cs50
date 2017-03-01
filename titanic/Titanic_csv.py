#import relevent packages
import csv as csv #for reading and writing csv files
import numpy as np #for maths and arrays
#calling function -> csv.[function] or np.[function]

""" import csv files to python file, then print the specific properties' statics"""
csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next() #skip table's header

data = []
for row in csv_file_object:
	data.append(row)	#each item viewd as a string under csv reader
data = np.array(data)

# print data[0]
# print data[-1]
# print data[0,3]
# print data[0::, 4]
# if i want to numerical calculation through csv reader, need to convert the type first

# print data[0:, 2]

""" .size() function can count the amount of elements """
number_passengers = np.size(data[0::, 1].astype(np.float))
number_survived = np.sum(data[0::, 1].astype(np.float))
proprtion_survivors = number_survived/ number_passengers

# print number_passengers
# print number_survived
# print proprtion_survivors

"""calculate with gender difference"""
# mask to determine gender
women_only_stats = data[0::, 4] == "female"
men_only_stats = data[0::, 4] != "female"
# .sum() addup numbers/ .size() addup exsisting items
women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)
proportion_women_survived = np.sum(women_onboard)/np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard)/ np.size(men_onboard)

# print proportion_women_survived
# print proportion_men_survived

# reading the test data and writing the gender model as a csv

# test_file = open('test.csv', 'rb')
# test_file_object = csv.reader(test_file)
# header = test_file_object.next()

# # creating csv file
# prediction_file = open('gernderbasemodel.csv', 'wb')
# prediction_file_object = csv.writer(prediction_file)

# # write survival prediction, paste to csv file we just created
# prediction_file_object.writerow(["PassengerId", "Survived"])
# for row in test_file_object:
# 	if row[3] == 'female':
# 		prediction_file_object.writerow([row[0], '1']) # predict 1
# 	else:
# 		prediction_file_object.writerow([row[0], '0']) # predict 0
# test_file.close()
# prediction_file.close()


"""created table, 1. arrange the cells model needed"""
fare_ceiling = 40 # ceiling, as a mask to deal with stats
# modify items which fare >= 40 to 39
data[ data[0::, 9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling/ fare_bracket_size

# same outcome, two ways
# number_of_classes = 3
number_of_classes = len(np.unique(data[0::, 2]))
# print number_of_classes
# print number_of_price_brackets
# .zeros(num_array, num_row, num_column) function can build a new array with 0 value in
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))

for i in xrange(number_of_classes):
	for j in xrange(number_of_price_brackets):
# data[ where function, 1] means it's finding the Survived column for the conditional criteria(multi-criteria) which is being called
		A_1 = (data[0::, 4] == "female")
		A_2 = (data[0::, 4] != "female")
		B = (data[0::, 2].astype(np.float) == i + 1)
		C = (data[0:, 9].astype(np.float) >= j * fare_bracket_size)
		D = (data[0:, 9].astype(np.float) < (j + 1) * fare_bracket_size)
		women_only_stats = data[A_1 & B & C & D, 1]
		men_only_stats = data[A_2 & B & C & D, 1]
		survival_table[0, i, j] = np.mean(women_only_stats.astype(np.float))
		survival_table[1, i, j] = np.mean(men_only_stats.astype(np.float))
		survival_table[ survival_table != survival_table] = 0

# for i in xrange(number_of_classes):       #loop through each class
# 	for j in xrange(number_of_price_brackets):   #loop through each price bin

# 	    women_only_stats = data[(data[0::, 4] == "female")\
# 	                       & (data[0::, 2].astype(np.float) == i + 1)\
# 	                       & (data[0:, 9].astype(np.float) >= j * fare_bracket_size)\
# 	                       & (data[0:, 9].astype(np.float) < (j + 1) * fare_bracket_size), 1] 	
# 	    men_only_stats = data[(data[0::, 4] != "female")\
# 	                       & (data[0::, 2].astype(np.float) == i + 1)\
# 	                       & (data[0:, 9].astype(np.float) >= j * fare_bracket_size)\
# 	                       & (data[0:, 9].astype(np.float) < (j + 1) * fare_bracket_size), 1]
# 	    survival_table[0, i, j] = np.mean(women_only_stats.astype(np.float))
# 	    survival_table[1, i, j] = np.mean(men_only_stats.astype(np.float))
# 	    survival_table[ survival_table != survival_table] = 0

# print survival_table

# transfer survival_table value with new criteria
survival_table[survival_table < 0.5] = 0
survival_table[survival_table >= 0.5] = 1

# print survival_table

test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()
predictions_file = open('genderclassmodel.csv', 'wb')
p = csv.writer(predictions_file)
p.writerow(['PassengerId', 'Survived'])

for row in test_file_object:
	for j in xrange(number_of_price_brackets):
		try:
			row[8] = float(row[8])
		except:
			bin_fare = 3 - float(row[1])
			break
		if row[8] > fare_ceiling:
			bin_fare = number_of_price_brackets - 1
			break
		if row[8] >= j * fare_bracket_size and row[8] < (j + 1) * fare_bracket_size:
			bin_fare = j
			break
		if row[3] == 'female':
			p.writerow([row[0], '%d' % int(survival_table[0, float(row[1]) - 1, bin_fare])])
		else:
			p.writerow([row[0], "%d" % int(survival_table[1, float(row[1]) - 1, bin_fare])])

# close out the files
test_file.close()
predictions_file.close()