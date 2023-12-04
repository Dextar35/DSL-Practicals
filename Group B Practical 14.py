"""
Write a python program to store first year percentage of students in an array.
Write function for sorting array of floating point numbers in ascending order
using:
    a) Selection Sort
    b) Bubble Sort and display top five scores
"""
#****************************************************************************

def Selection_Sort(marks):
    for i in range(len(marks)):
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j
        marks[i], marks[min_idx] = marks[min_idx], marks[i]
    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])

#****************************************************************************

def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])

#****************************************************************************

def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n")

#****************************************************************************

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
    print("1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Display top five scores")
    ch=int(input("\nEnter your choice (from 1 to 3) : "))
    if (ch == 1):
        Selection_Sort(marks)
    elif (ch == 2):
        Bubble_Sort(marks)
    elif (ch == 3):
        top_five_marks(marks)
    else:
        print ("Invalid choice")
    choice = input("\nDo you want to continue? (y/n) : ")
print ("\nThank You ..!")

#***************************END OF PROGRAM***********************************































    
