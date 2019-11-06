def Search(matrix,n,key):
    flag=0
    location=0
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]==key):
                flag=1
                location=i+1
                break;

    return flag,location


def sortRows(matrix,n):
    for i in range(n):
        matrix[i].sort()

def ColumnRotate(matrix,n):
    for i in range(n):
        for j in range(i+1,n):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i] =temp


def Sort_Row_Col(matrix,n):
    sortRows(matrix,n)

    ColumnRotate(matrix,n)

    sortRows(matrix,n)

    ColumnRotate(matrix,n)


def printmatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()
matrix=[[8,3,4,6,5],
        [6,7,3,4,1],
        [3,7,1,4,8],
        [9,2,6,3,9],
        [4,8,2,9,11]]
n=5
printmatrix(matrix,n)
print("-------------")
Sort_Row_Col(matrix,n)
printmatrix(matrix,n)
key=11

got,row=Search(matrix,n,key)
if(got==1):
    print("Element",key,"is located in row:",row)
else:
    print("Element",key,"not found")