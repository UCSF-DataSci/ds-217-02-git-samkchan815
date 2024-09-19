'''Find the sum of all the multiples of 3 or 5 below 1000.'''
sum = 0 # set a counter

for i in range(0, 1000): # loop through to values less than 1000
    if((i % 3 == 0) or (i % 5 == 0)): # check if multiple of 3 or 5
        sum += i # add to running sum

print(sum) # return running sum