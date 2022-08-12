# 3-measurement sliding window
# E.g. 

#   199  A      
#   200  A B    
#   208  A B C  
#   210    B C D 
#   200  E   C D
#   207  E F   D
#   240  E F G  
#   269    F G H
#   260      G H
#   263        H

# Compare 1st and 2nd windows
#   A (199, 200, 208) = 607 (sum)
#   B (200, 208, 210) = 618
# B is larger than A, so 1st comparison increased

# Count the number of times the sum of measurements in this sliding window increases from the previous sum

import csv

with open('input.txt') as f:
    list = [int(i) for i in f.read().split()]

i = 4 # start on index 4
answer = 0 # counts number of increases

while i <= len(list):
    
    if sum(list[i-3:i]) > sum(list[(i-4):(i-1)]): # sums current window with sum of prev window
        print(list[i-3:i], sum(list[i-3:i]), " > ", list[(i-4):(i-1)], sum(list[(i-4):(i-1)]))
        answer += 1
    
    i += 1

print("Answer: ", answer)