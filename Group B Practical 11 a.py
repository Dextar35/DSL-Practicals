"""Write a python program to store roll numbers of student in array who attended
   training program in random order. Write function for searching whether particular
   student attended training program or not using Linear search and Sentinel search"""
#**************************************************************************************

def linear_search(arr, n ,key):
    for i in range(0,n):
        if (arr[i] == key ):
            print ("Student attended the training program")
            return
    print ("Student not attended the training program")

#**************************************************************************************
    
def sentinel_search(arr, n, key):
    last = arr[n-1]
    arr[n-1] = key
    i = 0
    while (arr[i] != key):
        i += 1
    arr[n-1] = last
    if ((i < n-1) or (arr[n-1] == key)):
        print ("Student attended the training program")
    else:
        print ("Student not attended the training program")

#**************************************************************************************
        
arr=[]
n=int(input("Enter the number of students who attended the training program : "))
print ("Enter the roll numbers of students (Press enter after entering) : ")
for i in range(0,n):
    roll_no=int(input())
    arr.append(roll_no)
print ("The list of students roll number attended the training program : ")
print (arr)
choice = 'y'
while (choice == 'y' or choice =='Y'):
    key=int(input("Enter the roll number to find : "))
    print ("\n***********MENU***********")
    print ("1. Linear Search")
    print ("2. Sentinel Search")
    ch = int(input("Enter your choice : "))
    if (ch == 1):
        linear_search(arr, n, key)
    elif (ch == 2):
        sentinel_search(arr, n, key)
    else:
        print ("Invalid choice")
    choice = input("Do you want to continue (y/n) : ")
print ("Thank You..!")

#************************************END OF PROGRAM***************************************


