# Submarine performs a sonar sweep of the sea floor
# The sonar sweep report (your puzzle report) appears:
#   Each line is a measurement of the sea floor depth

# How quickly does the depth increase? 
# Do this by counting the number of times a depth measurement increases from the previous measurement.
# E.g.  There are 7 increases in the below sequence:
#   199 (N/A - no previous measurement)
#   200 (increased)
#   208 (increased)
#   210 (increased)
#   200 (decreased)
#   207 (increased)
#   240 (increased)
#   269 (increased)
#   260 (decreased)
#   263 (increased)

# Aim: How many measurements are larger than the previous measurement?

import csv

# read file as string, split string into integers, and add to list
with open('input.txt') as f:
    list = [int(i) for i in f.read().split()]

i = 1 # start on 2nd index
answer = 0 # counts number of increases

while i < len(list):
    
    if list[i] > list[i-1]: # counts number of increases if current index is larger than previous
        answer += 1
        print("Index: ", i, "Check: ", list[i], list[i-1], "Increase count: ", answer)
    else:
        print("Index: ", i, "Check: ", list[i], list[i-1], "Increase count: ", answer, " DECREASE")

    i += 1

print("Answer: ", answer)