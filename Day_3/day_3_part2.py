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

# Get Oxygen Generator Rating number
i = 0
while len(o2_data) != 1: # repeats until one number remains
    zero_total = 0
    one_total = 0
    
    # determine count of zeros and ones for the corresponding index
    for item in o2_data:
        if item[i] == '0':
            zero_total += 1
        else:
            one_total += 1
    
    # check most common and then keep most common
    if (zero_total > one_total): # keep 0's and remove 1's
        j=0
        while len(o2_data) > j: # sequencially check all numbers once
            if o2_data[j][i] == '1': # checks the bit of the number
                del(o2_data[j])
            else:
                # prevent j index from increasing when an item is removed
                # because when an element is removed, the index of remaining list is reduced by 1
                # otherwise it would skip the next index
                j+=1 
    elif (zero_total < one_total) or (zero_total == one_total): # keep 1's and remove 0's
        j=0
        while len(o2_data) > j:
            if o2_data[j][i] == '0':
                del(o2_data[j])
            else:
                j+=1

    i += 1

# Get CO2 Generator Rating number
# Similar function as the while loop for Oxygen Generator Rating number (above)
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
    
    # check least common and then keep least common
    if (zero_total > one_total): # keep 1's and remove 0's
        j=0
        while len(co2_data) > j:
            if co2_data[j][i] == '0':
                del(co2_data[j])
            else:
                j+=1
    elif (zero_total < one_total) or (zero_total == one_total): # keep 0's and remove 1's
        j=0
        while len(co2_data) > j:
            if co2_data[j][i] == '1':
                del(co2_data[j])
            else:
                j+=1

    i += 1

# convert arrays to string (binary numbers)
o2_gen_rating = str(o2_data).replace("'",'').replace('[', '').replace(']', '').replace(' ','')
co2_gen_rating = str(co2_data).replace("'",'').replace('[', '').replace(']', '').replace(' ','')

# convert binary to decimal
o2_gen_rating = int(o2_gen_rating, 2)
co2_gen_rating = int(co2_gen_rating, 2)

life_support_rating = o2_gen_rating * co2_gen_rating

print("Oxygen Generator Rating: ", o2_data, "= ", o2_gen_rating)
print("CO2 Generator Rating: ", co2_data, "= ", co2_gen_rating)
print("Life Support Rating = ", life_support_rating)