# Initial 3x3 matrix filled with zeros
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Replace the main diagonal elements with 1
for i in range(3):
    matrix[i][i] = 1

# Print the modified matrix
for row in matrix:
    print(*row)

