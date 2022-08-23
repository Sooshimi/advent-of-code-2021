# - Consider just the 1st bit of numbers
# - Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. 
#   Discard numbers which do not match the bit criteria.
# - If you only have one number left, stop; this is the rating value for which you are searching.
# - Otherwise, repeat the process, considering the next bit to the right.

# The bit criteria depends on which type of rating value you want to find:
# - To find oxygen generator rating: determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
#   If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# - To find CO2 scrubber rating: determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
#   If 0 and 1 are equally common, keep values with a 0 in the position being considered.

with open('Day_3/input.txt') as f:
    data = [str(i) for i in f.read().split("\n")]

o2_data = data.copy()
co2_data = data.copy()

i = 0

while len(o2_data) != 1:
    zero_total = 0
    one_total = 0
    
    # determine count of zeros and ones for the corresponding index
    for item in o2_data:
        
        # if i == len(item):
        #     break

        if item[i] == '0':
            zero_total += 1
        else:
            one_total += 1
    
    # check most common and then keep most common
    
    # keep 0's and remove 1's
    if (zero_total > one_total):
        for item in o2_data:
            if item[i] == '1':
                o2_data.remove(item)
    
    # keep 1's and remove 0's
    elif (zero_total < one_total) or (zero_total == one_total):
        for item in o2_data:
            if item[i] == '0':
                o2_data.remove(item)

    i += 1
    
    if i == len(item):
        i = 0

i = 0

while len(co2_data) != 1:
    
    zero_total = 0
    one_total = 0
    
    # determine count of zeros and ones for the corresponding index
    for item in co2_data:

        if item[i] == '0':
            zero_total += 1
        else:
            one_total += 1
    
    # check most common and then keep least common
    
    # keep 1's and remove 0's
    if (zero_total > one_total):
        for item in co2_data:
            if item[i] == '0':
                co2_data.remove(item)
    
    # keep 0's and remove 1's
    elif (zero_total < one_total) or (zero_total == one_total):
        for item in co2_data:
            if item[i] == '1':
                co2_data.remove(item)

    i += 1
    
    if i == len(item):
        i = 0

print(o2_data)
print(co2_data)

# convert gamma/epsilon arrays to string (binary numbers)
o2_gen_rating = str(o2_data).replace("'",'').replace('[', '').replace(']', '').replace(' ','')
co2_gen_rating = str(co2_data).replace("'",'').replace('[', '').replace(']', '').replace(' ','')

# convert binary to decimal
o2_gen_rating = int(o2_gen_rating, 2)
co2_gen_rating = int(co2_gen_rating, 2)

life_support_rating = o2_gen_rating * co2_gen_rating

print("Life Support Rating = ", life_support_rating)