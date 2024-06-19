# For loop operations with list 

list03 = [1,2,3,4,5,6]
total = 0

for i in range(len(list03)):
    total += list03[i]

print(total)

total2 = 0

for i in list03:
    total2 += i 

print(total2)