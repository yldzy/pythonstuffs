import numpy as np

#initials
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

namepos = ['First Name', 'Middle Name', 'Last Name']

pos = ['first', 'second', 'third']

inputs = []
array1 = []
array2 = []
array3 = []
array4 = []

#inputs
print("INPUT THE INITIALS OF YOUR NAME\n")

for i in range(3):
    ini = input(f"Enter your {namepos[i]} initial: ")
    inputs.append(ini)

#second letter of name
print("\nINPUT THE 2ND LETTER OF YOUR NAME\n")

for i in range(3):
    ini = input(f"Enter the 2nd letter of your {namepos[i]}: ")
    inputs.append(ini)
    
#first 2 arrays
for x in range(len(inputs)):
    for i in range(len(alphabet)):
        if alphabet[i] == inputs[x].casefold():
            if x < 3:
                array1.insert(x, i + 1)
            elif x > 2:
                array2.insert(x, i + 1)

#student number first 3
print("\nINPUT THE FIRST 3 NUMBERS OF YOUR STUDENT NUMBER\n")

for i in range(3):
    ini = int(input(f"Enter the {pos[i]} number: "))
    array3.append(ini)

#student number last 3
print("\nINPUT THE LAST 3 NUMBERS OF YOUR STUDENT NUMBER\n")

for i in range(3):
    ini = int(input(f"Enter the {pos[i]} number: "))
    array4.append(ini)

#matrix 1
matrix1 = [array1, array2]
print('\nMATRIX 1: \n')
for i in range(2):
    for j in range(3):
        print(matrix1[i][j], end=" ")
    print()

#matrix 2
matrix2 = [array3, array4]
print('\nMATRIX 2: \n')
for i in range(2):
    for j in range(3):
        print(matrix2[i][j], end=" ")
    print()
    
#matrix3
matrix3 = np.add(matrix1, matrix2)
x = np.sum(matrix3)
print('\nMATRIX 3: SUM OF MATRIX 1 & MATRIX 2 \n')
for i in range(2):
    for j in range(3):
        print(matrix3[i][j], end=" ")
    print()

#matrix4
matrix4 = np.multiply(matrix1, 2)
print('\nMATRIX 4: MATRIX 1 MULTIPLIED BY 2 \n')
for i in range(2):
    for j in range(3):
        print(matrix4[i][j], end=" ")
    print()
    
#matrix5
print('\nMATRIX 5: MATRIX 2 TRANSPOSED\n')
matrix5 = np.transpose(matrix2)
for i in range(3):
    for j in range(2):
        print(matrix5[i][j], end=" ")
    print()
    
#matrix6
matrix6 = matrix3
print('\nMATRIX 6: PRODUCT OF MATRIX 3 & MATRIX 5\n')
for i in range(2):
    for j in range(2):
        matrix6[i][j] = matrix3[i][j] * matrix5[i][j]
        print(matrix6[i][j], end=" ")
    print()

#sum of matrix3
print("\nThe sum of all elements in Matrix 3 is: ", x)

#matrix7
matrix7 = np.zeros((2, 3), dtype = int)
print('\nMATRIX 7: ZERO MATRIX\n')
for i in range(2):
    for j in range(3):
        print(matrix7[i][j], end=" ")
    print()
