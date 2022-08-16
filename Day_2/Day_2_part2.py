# down X increases aim by X units
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.


# read file as string, split string into integers
with open('Day_2/input.txt') as f:
    data = [str(i) for i in f.read().split("\n")]

list = [] # empty list
forward = 0 # keeps track of horizontal position
depth = 0 # keeps track of depth
aim = 0 # keeps track of aim

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
            if aim > 0:
                depth += (aim * value)
        if key == "up":
            aim -= value
        if key == "down":
            aim += value

answer = forward * depth

print("Forward: ", forward)
print("Depth: ", depth)
print("Aim: ", aim)
print("Answer: ", answer)