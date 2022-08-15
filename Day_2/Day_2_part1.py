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

##########################################################################################################

# read file as string, split string into integers
with open('Day_2/input.txt') as f:
    data = [str(i) for i in f.read().split("\n")]

list = [] # empty list
forward = 0 # keeps track of horizontal position
depth = 0 # keeps track of depth

# create list of key value pairs
for i in data:
    item = {} # empty item, empties on next iteration
    i = i.split(" ") # split item by space
    key, value = i[0], int(i[1]) # create key and value variables
    item[key] = value # map key value pair into item object
    list.append(item) # append item into list

# iterate for all items in list
for i in list:
    for key, value in i.items(): # iterate for all key value pairs
        if key == "forward":
            forward += value
        if key == "up":
            depth -= value
        if key == "down":
            depth += value

answer = forward * depth

print("Forward: ", forward)
print("Depth: ", depth)
print("Answer: ", answer)