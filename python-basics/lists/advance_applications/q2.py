# Creating a 3D array (tensor)
tensor = [
    [
        [1, 2], [3, 4]
    ],
    [
        [5, 6], [7, 8]
    ]
]

# Accessing an element
print(tensor[1][0][1])  # Output: 6

# Iterating over a 3D array
for matrix in tensor:
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
    print()
