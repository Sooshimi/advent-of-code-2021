# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

# input.txt shows the planned course

# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:
#   forward 5 adds 5 to your horizontal position, a total of 5.
#   down 5 adds 5 to your depth, resulting in a value of 5.
#   forward 8 adds 8 to your horizontal position, a total of 13.
#   up 3 decreases your depth by 3, resulting in a value of 2.
#   down 8 adds 8 to your depth, resulting in a value of 10.
#   forward 2 adds 2 to your horizontal position, a total of 15.

# After following these instructions, you would have a horizontal position 
# of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

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