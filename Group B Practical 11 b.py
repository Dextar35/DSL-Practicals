"""Write a python program to store roll numbers of student in array who attended
   training program in sorted order. Write function for searching whether particular
   student attended training program or not using Binary search and Fibonacci search"""
#**************************************************************************************

def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            print ("Student attended the training program")
            return 
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    print ("Student not attended the training program")
    return

#**************************************************************************************

def fibonacci_search(arr, n, x):      
    m2 = 0   
    m1 = 1   
    m = m2 + m1    
    while (m < n): 
        m2 = m1 
        m1 = m 
        m = m2 + m1 
    offset = -1
    while (m > 1): 
        i = min(offset+m2, n-1)  
        if (arr[i] < x): 
            m = m1 
            m1 = m2 
            m2 = m - m1 
            offset = i 
        elif (arr[i] > x): 
            m = m2 
            m1 = m1 - m2 
            m2 = m - m1 
        else:
            print ("Student attended the training program")
            return 
    if(m1 and arr[n-1] == x): 
        return n-1
    print ("Student not attended the training program")
    return

#**************************************************************************************

arr=[]
n=int(input("Enter the number of students who attended the training program : "))
print ("Enter the roll numbers of students (Press enter after entering) : ")
print ("(Enter the roll numbers in sorted order)")
for i in range(0,n):
    roll_no=int(input())
    arr.append(roll_no)
print ("The list of students roll number attended the training program : ")
print (arr)
choice = 'y'
while (choice == 'y' or choice =='Y'):
    key=int(input("Enter the roll number to find : "))
    print ("\n***********MENU***********")
    print ("1. Binary Search")
    print ("2. Fibonacci Search")
    ch = int(input("Enter your choice : "))
    if (ch == 1):
        binary_search(arr, 0, n-1, key)
    elif (ch == 2):
        fibonacci_search(arr, n, key)
    else:
        print ("Invalid choice")
    choice = input("Do you want to continue (y/n) : ")
print ("Thank You..!")

#************************************END OF PROGRAM***************************************