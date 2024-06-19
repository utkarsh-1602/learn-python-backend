list01 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = 10

for i in range(0, len(list01)):
    if list01[i] > largest:
        largest = list01[i]

print(largest)