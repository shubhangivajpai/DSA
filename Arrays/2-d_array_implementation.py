R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row-wise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
    
#Python (Method 2)
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row-wise:")

# For user input
matrix = [[int(input()) for x in range(C)] for y in range(R)]


# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
