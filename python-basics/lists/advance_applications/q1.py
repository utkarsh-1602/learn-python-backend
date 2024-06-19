# Creating a 2D array (matrix) with 3 rows and 3 columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element
print(matrix[1][2])  # Output: 6

# Iterating over a 2D array
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
