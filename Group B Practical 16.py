"""
Write a Python program to store first year percentage of students in array. Write
function for sorting of floating point numbers in ascending order using quick
sort and display top five scores.
"""
#*******************************************************************************

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

#*******************************************************************************

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

#*******************************************************************************
        
def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n")

#*******************************************************************************

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)
print("The marks of",n,"students are : ")
print(marks)
choice = 'y'
while (choice == 'y' or choice == 'Y'):
    print("\n***************MENU***************")
    print("1. Quick Sort of the marks")
    print("2. Display top five scores")
    ch=int(input("\nEnter your choice (from 1 to 3) : "))
    if (ch == 1):
        quicksort(marks, 0, n-1)
        print ("Sorted array : ")
        for x in marks:
            print(x)
    elif (ch == 2):
        top_five_marks(marks)
    else:
        print ("Invalid choice")
    choice = input("\nDo you want to continue? (y/n) : ")
print ("\nThank You ..!")

#********************************END OF PROGRAM*********************************
