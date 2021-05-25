#1.Write a  program to add two matrices.
'''
matrix_first=[]
matrix_second=[]
row=int(input("Enter the Row : "))
column=int(input("Enter the Column : "))

#user input for first matrix
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_first.append(temp_matrix)

#user input for second matrix 
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_second.append(temp_matrix)
    
matrix_third=[]

#Adding two matrix

for i in range(row):
    temp_matrix=[]
    for j in range(column):
        temp_matrix.append(matrix_first[i][j]+matrix_second[i][j])
    matrix_third.append(temp_matrix)
        

    
#printing first matrix
print("First Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_first[i][j],end=' ' )
    print()

print()
#printing second matrix
print("Second Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_second[i][j],end=' ' )
    print()

print()
#printing adding  matrix result
print("Result Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_third[i][j],end=' ' )
    print()
'''

#2.Write a  program to subtract two matrices.
'''

matrix_first=[]
matrix_second=[]
row=int(input("Enter the Row : "))
column=int(input("Enter the Column : "))

#user input for first matrix
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_first.append(temp_matrix)

#user input for second matrix 
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_second.append(temp_matrix)
    
matrix_third=[]

#Adding two matrix

for i in range(row):
    temp_matrix=[]
    for j in range(column):
        temp_matrix.append(matrix_first[i][j]-matrix_second[i][j])
    matrix_third.append(temp_matrix)
        

    
#printing first matrix
print("First Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_first[i][j],end=' ' )
    print()

print()
#printing second matrix
print("Second Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_second[i][j],end=' ' )
    print()

print()
#printing adding  matrix result
print("Result Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_third[i][j],end=' ' )
    print()

'''

#3.Write a program to perform Scalar matrix multiplication.
'''
matrix_first=[]
matrix_result=[]
row=int(input("Enter the Row : "))
column=int(input("Enter the Column : "))

#user input for first matrix
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_first.append(temp_matrix)

#Multiplying number

n=int(input("Enter the number to multiply matrix : "))

#multiply  two matrix

for i in range(row):
    temp_matrix=[]
    for j in range(column):
        temp_matrix.append(n*matrix_first[i][j])
    matrix_result.append(temp_matrix)
        
#printing first matrix
print("First Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_first[i][j],end=' ' )
    print()

print()
#printing adding  matrix result
print("Result Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_result[i][j],end=' ' )
    print()

'''

#4.Write a  program to check whether two matrices are equal or not.
'''
matrix_first=[]
matrix_second=[]
row=int(input("Enter the Row : "))
column=int(input("Enter the Column : "))

#user input for first matrix
print("Input for First Matrix")
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_first.append(temp_matrix)

#user input for second matrix
print("Input for Second Matrix")
for i in range(row):
    temp_matrix=[]
    for j in range(column):
        elements=int(input("Enter the elements : "))
        temp_matrix.append(elements)
    matrix_second.append(temp_matrix)
    
is_equal=0
#checking condition

for i in range(row):
    for j in range(column):
        if matrix_first[i][j] == matrix_second[i][j]:
            is_equal=1
            break;  
#printing first matrix
print("First Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_first[i][j],end=' ' )
    print()

print()
#printing second matrix
print("Second Matrix")
for i in range(row):
    for j in range(column):
        print(matrix_second[i][j],end=' ' )
    print()

if is_equal==1:
    print("Both Matrix are Equal")
else:
     print("Matrix are not Equal")
'''

#5.Write a program to multiply two matrices.
'''
matrix_first=[]
matrix_second=[]
first_matrix_row=int(input("Enter the First Matrix Row : "))
first_matrix_column=int(input("Enter the First Matrix Column : "))
second_matrix_row=int(input("Enter the Second Matrix Row : "))
seocnd_matrix_column=int(input("Enter the Second Matrix Column : "))

while first_matrix_column != second_matrix_row:
    print("First Matrix Column and Second Matrix Row is not same.\n(It is out of Matrix Multiplication Rules")
    
    first_matrix_row=int(input("Enter the First Matrix Row : "))
    first_matrix_column=int(input("Enter the First Matrix Column : "))
    second_matrix_row=int(input("Enter the Second Matrix Row : "))
    seocnd_matrix_column=int(input("Enter the Second Matrix Column : "))


        

#user input for first matrix
for i in range(first_matrix_row):
    temp_matrix=[]
    for j in range(first_matrix_column):
        elements=int(input("Enter the elements for First Matrix : "))
        temp_matrix.append(elements)
    matrix_first.append(temp_matrix)

#user input for second matrix 
for i in range(second_matrix_row):
    temp_matrix=[]
    for j in range(seocnd_matrix_column):
        elements=int(input("Enter the elements for Second Matrix: "))
        temp_matrix.append(elements)
    matrix_second.append(temp_matrix)
    
matrix_third=[]

#multiplying two matrix

for i in range(first_matrix_row):

    temp_matrix=[]
    for j in range(seocnd_matrix_column):
        dot=0
        for k in range(seocnd_matrix_column):
            dot=dot+matrix_first[i][k]*matrix_second[k][j]
        temp_matrix.append(dot)
    matrix_third.append(temp_matrix)
        

    
#printing first matrix
print("First Matrix : ")
for i in range(first_matrix_row):
    for j in range(first_matrix_column):
        print(matrix_first[i][j],end=' ' )
    print()

print()
#printing second matrix
print("Second Matrix : ")
for i in range(second_matrix_row):
    for j in range(seocnd_matrix_column):
        print(matrix_second[i][j],end=' ' )
    print()

print()
#printing multiplication  matrix result
print("Result Matrix : ")
for i in range(first_matrix_row):
    for j in range(seocnd_matrix_column):
        print(matrix_third[i][j],end=' ' )
    print()

'''
#6.Write a  program to find sum of main diagonal elements of a matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)

for i in range(row):
    for j in range(col):
        if i==j:
            sum=sum+matrix[i][j]

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

print("Sum of Main diagonal: ",sum)

'''

#6.Write a  program to find sum of minor diagonal elements of a matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)

for i in range(row):
    for j in range(col):
        if i+j==row-1:
            sum=sum+matrix[i][j]

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

print("Sum of Opposite diagonal: ",sum)

'''
#7.Write a  program to find sum of each row and column of a matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)


for i in range(row):
    sum_of_row=0
    for j in range(col):
            sum_of_row=sum_of_row+matrix[i][j]
    print("Sum of Row : " ,sum_of_row)

for i in range(row):
    sum_of_column=0
    for j in range(col):
            sum_of_column=sum_of_column+matrix[j][i]
    print("Sum of Column : " ,sum_of_column)

'''

#8.Write a  program to interchange diagonals of a matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)
    
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

print("Interchange matrix : ")

n=col-1

for i in range(row):
    for j in range(col):
        if i==j:
            temp=matrix[i][j]
            matrix[i][j]=matrix[i][n]
            matrix[i][n]=temp
            n=n-1

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

'''
            
#9.Write a  program to find sum of upper triangular matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)

for i in range(row):
    for j in range(col):
        if i<j:
            sum=sum+matrix[i][j]

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

print("Sum of upper triangular matrix : ",sum)

'''

#10.Write a  program to find sum of lower triangular matrix.

'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)

for i in range(row):
    for j in range(col):
        if i>j:
            sum=sum+matrix[i][j]

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()

print("sum of lower triangular matrix : ",sum)

'''

#11.Write a  program to find upper triangular matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)


for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()
print("Upper triangular : ")
for i in range(row):
    for j in range(col):
        if i<j:
            print(matrix[i][j],end='   ')
            
    print()
    print(end='    ')
'''

#12.Write a  program to find Lower triangular matrix.
'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)


for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=' ' )
    print()
print("Lower triangular : ")
for i in range(row):
    for j in range(col):
        if i>j:
            print(matrix[i][j],end='   ')
            
    print()
    print(end='    ')

'''

#13.Write a  program to find transpose of a matrix.

'''
matrix=[]
sum=0
row=int(input("Enter the row size :"))
col=int(input("Enter the column size : "))

for i in range(row):
    temp_matrix=[]
    for j in range(col):
        elements=int(input("Enter the Elements : "))
        temp_matrix.append(elements)
    matrix.append(temp_matrix)


for i in range(row):
    for j in range(col):
        print(matrix[i][j],end='  ' )

    print()


print("Transpose of  Matrix : ")

transpose_matrix=[]

for i in range(row):
    temp_transpose_matrix=[]
    for j in range(col):
        temp_transpose_matrix.append(matrix[j][i])
        
    transpose_matrix.append(temp_transpose_matrix)
    
for i in range(row):
    for j in range(col):
        print(transpose_matrix[i][j],end='  ' )

    print()

'''












