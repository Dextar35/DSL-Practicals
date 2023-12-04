def average(m):
    sum=0
    cnt=0
    for i in range(len(m)):
        if m[i]!=-999:
            sum+=m[i]
            cnt+=1
    avg=sum/cnt
    print("Average Marks : {:.2f}".format(avg))
#************************************************************************
def maximum(m):
    for i in range(len(m)):
        if m[i]!=-999:
            Max=m[0]
            break
    for i in range(1,len(m)):
        if m[i]>Max:
            Max=m[i]
    return(Max)
#************************************************************************
def minimum(m):
    for i in range(len(m)):
        if m[i]!=-999:
            Min=m[0]
            break
    for i in range(1,len(m)):
        if m[i]<Min:
            Min=m[i]
    return(Min)
#************************************************************************
def absentcount(m):
    cnt=0
    for i in range(len(m)):
        if m[i]==-1:
            cnt+=1
    return(cnt)
#************************************************************************
def maxFrequency(m):
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in m:
        if (m.index(j)==i):
            print(j,"    |  ",m.count(j))
            if m.count(j)>Max:
                Max=m.count(j)
                mark=j
        i=i+1
    return(mark,Max)
#***********************************************************************
FDS=[]
nos=int(input("Enter total number of students : "))
print ("Enter -1 if absent")
for i in range(nos):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    FDS.append(marks)
choice=1
while choice==1:
    print("\n\n********************MENU********************\n")
    print("1. Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    ch=int(input("Enter your Choice (from 1 to 4) :"))
    if ch==1:
        average(FDS)
    elif ch==2:
        print("Highest Score in Class : ", maximum(FDS))
        print("Lowest Score in Class : ", minimum(FDS))
    elif ch==3:
        print("Number of Students absent in the test : ", absentcount(FDS))
    elif ch==4:
        mark,fr = maxFrequency(FDS)
        print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))
    else:
        print("Invalid Choice")
    a=input("Do you want to continue (yes/no) :")
    if a=="yes":
        choice=1
    else:
        choice=0
        print("Thanks for using this program!")
#***************************END OF PROGRAM*******************************
