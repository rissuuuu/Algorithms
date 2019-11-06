def Search(matrix,n):
    flag=0
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]==0):
                flag+=1
    return flag


def sortRowsAscending(matrix,n):
    for i in range(n):
        for j in range(n-1):
            if(matrix[i][j]>matrix[i][j+1]):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][j+1]
                matrix[i][j+1]=temp

def sortColsDescending(matrix,n):
    for i in range(n):
        for j in range(n-1):
            if(matrix[i][j]<matrix[i][j+1]):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][j+1]
                matrix[i][j+1]=temp

def ColumnRotate(matrix,n):
    for i in range(n):
        for j in range(i+1,n):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i] =temp

def Sort_Row_Col(matrix,n):
    sortRowsAscending(matrix,n)
    printmatrix(matrix,n)
    ColumnRotate(matrix,n)
    print("_______________")
    sortColsDescending(matrix,n)
    printmatrix(matrix,n)
    ColumnRotate(matrix,n)

def printmatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

matrix=[[1,3,-4],
        [-1,0,3],
        [3,0,-9]]
n=3
printmatrix(matrix,n)
print("-------------")
Sort_Row_Col(matrix,n)
got=Search(matrix,n)

print("Element 0 is ",got)
