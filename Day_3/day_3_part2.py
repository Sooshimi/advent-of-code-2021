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

zero_total = [0,0,0,0,0,0,0,0,0,0,0,0] # counts number of zeros for each corresponding index
one_total = [0,0,0,0,0,0,0,0,0,0,0,0] # counts number of ones for each corresponding index
gamma_rate_array = [] # holds most common bit of numbers for gamma rate
epsilon_rate_array = [] # holds most common bit of numbers for epsilon rate

for i in data:
    
    # iterate for bit of each row from the diagnostic report
    for index, bit in enumerate(list(i)):
        
        if int(bit) == 0:
            zero_total[index] += 1 # add one to the corresponding index if 0
        if int(bit) == 1:
            one_total[index] += 1 # add one to the corresponding index if 1

# compares the count of 0 and 1's from both zero_total and one_total arrays, and appends the most
# common value to the correponding index in gamma or epsilon array, depending on the most common value
for index, n in enumerate(range(len(zero_total))):
    if zero_total[index] > one_total[index]:
        gamma_rate_array.append(0)
        epsilon_rate_array.append(1) # epsilon is inverse of gamma
    else:
        gamma_rate_array.append(1)
        epsilon_rate_array.append(0)

# convert gamma/epsilon arrays to string (binary numbers)
gamma_rate = str(gamma_rate_array).replace(',','').replace('[', '').replace(']', '').replace(' ','')
epsilon_rate = str(epsilon_rate_array).replace(',','').replace('[', '').replace(']', '').replace(' ','')

# convert binary to decimal
gamma_dec = int(gamma_rate, 2)
epsilon_dec = int(epsilon_rate, 2)

power_consumption = gamma_dec * epsilon_dec

print(power_consumption)