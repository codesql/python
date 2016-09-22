#https://developers.google.com/edu/python/regular-expressions?hl=en
import re
 # Open file
#hand = open('regex_sum_42.txt')
hand = open('regex_sum_190602.txt')
numlist = list()
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall('([0-9]+)', hand.read())
print type(strings)
print strings
#Loop through the string to list, convert the into float then sum them up.
for line in strings:
    print line
    num = float(line)
    numlist.append(num)
print 'Sum:', sum(numlist)
#print strings
