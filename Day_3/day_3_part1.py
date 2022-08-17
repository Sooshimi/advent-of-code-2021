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