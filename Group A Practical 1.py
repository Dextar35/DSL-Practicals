def removeDuplicate(d):
    l=[]
    for i in d:
        if i not in l:
            l.append(i)
    return l
#******************************************************************************************************************
def intersection(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3
#*******************************************************************************************************************
def union(l1,l2):
    l3=l1.copy()
    for i in l2:
        if i not in l3:
            l3.append(i)
    return l3
#*******************************************************************************************************************
def diff(l1,l2):
    l3=[]
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3
#********************************************************************************************************************
def sym_diff(l1,l2):
    l3=[]
    D1=diff(l1,l2)
    print("Difference between Cricket and Badminton (C-B) is : ", D1)
    D2=diff(l2,l1)
    print("Difference between Badminton and Cricket (B-C) is : ", D2)
    l3=union(D1,D2)
    return l3
#*********************************************************************************************************************
SE_Comp = []
n = int(input("\nEnter number of students in SE COMP: "))
print("Enter the names of",n,"students (Please press ENTER after entering each students name) :")
for i in range(0, n):
    name = input()
    SE_Comp.append(name)  
print("Original list of students in SEComp : " + str(SE_Comp))
#**********************************************************************************************************************
Cricket = []
n = int(input("\n\nEnter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket (Please press ENTER after entering each students name) :")
for i in range(0, n):
    name = input()
    Cricket.append(name)  
print("Original list of students playing cricket is :" +str(Cricket))
Cricket=removeDuplicate(Cricket)
print("The list of students playing cricket after removing duplicates : " +str(Cricket))
#***********************************************************************************************************************
Football = []
n = int(input("\n\nEnter number of students who play football : "))
print("Enter the name of",n,"students who play football (Please press ENTER after entering each students name) :")
for i in range(0, n):
    name = input()
    Football.append(name)  
print("Original list of students playing football :" +str(Football))
Football=removeDuplicate(Football)
print("The list of students playing football after removing duplicates : " +str(Football))
#************************************************************************************************************************
Badminton = []
n = int(input("\n\nEnter number of students who play badminton : "))
print("Enter the name of",n,"students who play badminton (Please press ENTER after entering each students name) :")
for i in range(0, n):
    name = input()
    Badminton.append(name)  
print("Original list of students playing badminton :" +str(Badminton))
Badminton=removeDuplicate(Badminton)
print("The list of students playing badminton after removing duplicates : " +str(Badminton))
#*************************************************************************************************************************
choice=1
while choice==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. Number of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    ch=int(input("Enter your Choice (from 1 to 4) :"))
    if ch==1:
        print("List of students who play both cricket and badminton : ", intersection(Cricket,Badminton))
    elif ch==2:
        print("List of students who play either cricket or badminton but not both : ", sym_diff(Cricket,Badminton))  
    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", len(diff(SE_Comp,union(Cricket,Badminton))))        
    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", len(diff(intersection(Cricket,Football),Badminton)))        
    else:
        print("Thanks for using this program!")
    a = input("\n\nDo you want to continue (yes/no) :")
    if a == "yes":
        choice = 1
    else:
        choice = 0
        print("Thanks for using this program!")
#****************************************************END OF PROGRAM************************************************
