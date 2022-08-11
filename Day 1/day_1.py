# Submarine performs a sonar sweep of the sea floor
# The sonar sweep report (your puzzle report) appears:
#   Each line is a measurement of the sea floor depth

# How quickly does the depth increase? 
# Do this by counting the number of times a depth measurement increases from the previous measurement.
# E.g. 
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

with open('input.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    input = list(reader)
array = input

i = 1
answer = 0

while i < len(array):
    
    if array[i] > array[i-1]:
        answer += 1
        print("Index: ", i, "Check: ", array[i], array[i-1], "Answer: ", answer)
    else:
        print("Index: ", i, "Check: ", array[i], array[i-1], "Answer: ", answer, " DECREASE")
    
    i += 1

print(array[0])
print(array[len(array)-1])
print("Length: ", len(array))
print("Answer: ", answer)