rows1 = int(input("Enter Rows for Matrix 1 : "))
cols1 = int(input("Enter Columns for Matrix 1 : "))
mat1 = []
for i in range(rows1):
    l1 = []
    for j in range(cols1):
        l1.append(int(input("Enter Element mat1[%d][%d] : "%(i,j))))
    mat1.append(l1)
print()
rows2 = int(input("Enter Rows for Matrix 2 : "))
cols2 = int(input("Enter Columns for Matrix 2 : "))
mat2 = []
for i in range(rows2):
    l2 = []
    for j in range(cols2):
        l2.append(int(input("Enter Element mat2[%d][%d] : "%(i,j))))
    mat2.append(l2)
print("You have created following matrixes,")
print("Matrix 1 = ")
for i in range(rows1):
    for j in range(cols1):
        print("\t ",mat1[i][j],end=" ")
    print()
print("Matrix 2 =")
for i in range(rows2):
    for j in range(cols2):
        print("\t ",mat2[i][j],end=" ")
    print()

ch = 1
while(ch==1):
    choice = int(input("Enter 1)Addtion of Matrices.\n2)Subtraction of Matrices.\n3)Multiplication of Matrices\n4) for Transpose of a matrix\nEnter Choice = "))


    if (choice==1):
        if (rows1!=rows2 or cols1!=cols2):
            print("For Addition of Matrices rows and columns should be equal") 

        else:
            sum = []
            for i in range(rows1):
                s = []
                for j in range(rows2):
                    s.append(mat1[i][j]+mat2[i][j])
                sum.append(s)
            print("Resultant Matrix :")
            for i in range(rows1):
                for j in range(cols1): 
                    print("\t ",sum[i][j],end=" ")
                print()
                
                
    elif (choice==2):
        if (rows1!=rows2 or cols1!=cols2):
            print("For Subtraction of Matrices rows and columns should be equal") 

        else:
            diff = []
            for i in range(rows1):
                d = []
                for j in range(rows2):
                    d.append(mat1[i][j]-mat2[i][j])
                diff.append(d)
            print("Resultant Matrix :")
            for i in range(rows1):
                for j in range(cols1): 
                    print("\t",diff[i][j],end=" ")
                print()
                
    
    elif (choice==3):
        if(cols1 != rows2):
            print("Both Matix doesn't satisfies the condition of multiplication.")
        else:
            promat = []
            rows = rows1
            cols = cols2
            for i in range(rows):
                m = []
                for j in range(cols):
                    res = 0
                    for k in range(cols):
                        res += mat1[i][k] * mat2[k][j]
                    m.append(res)
                promat.append(m)
            print("Resultant Matrix :")
            for i in range(rows1):
                for j in range(cols2): 
                    print("\t ",promat[i][j],end=" ")
                print()
    elif (choice==4):
        transposed = []
        opt2 = int(input("1)Matrix 1\n2)Matrix 2\nYour Choice : "))
        if (opt2==1):
            for i in range(rows1):
                t = []
                for j in range(cols1):
                    t.append(mat1[j][i])
                transposed.append(t)
            print("Transposed Matrix :")
            for i in range(rows1):
                for j in range(cols1):
                    print("\t ",transposed[i][j],end=" ")
                print()
        else:
            for i in range(rows2):
                t = []
                for j in range(cols2):
                    t.append(mat2[j][i])
                transposed.append(t)
            print("Transposed Matrix:")
            for i in range(rows2):
                for j in range(cols2):
                    print("\t ",transposed[i][j],end=" ")
                print()
    else:
        print("Invalid Input")
    ch = int(input("Do You want to continue ?\n1)Yes\n2)No\nYour Response = "))