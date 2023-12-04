def longestword(str):
    list1=str.split()
    lword=list1[0]
    for i in range(len(list1)):
        if (len(list1[i])>len(lword)):
            lword=list1[i]
    return lword
def freqofchar(str):
    c=input("Enter the character to check its frequency : ")
    cnt=0
    for i in range(len(str)):
        if (c==str[i]):
            cnt+=1
    print ("Frequency of ",c,"is",cnt)
def palindrome(str):
    str1=str[::-1]
    if (str==str1):
        print ("Given string is palindrome")
    else:
        print ("Given string is not palindrome")
def indexofsubstring(str):
    substr=input("Enter the substring : ")
    for i in str:
        if (i==substr):
            print ("Substring found")
            print ("Index of substring is",str.index(substr))
            return
    print ("Substring not found")
def occurencesofword(str):
    list1=str.split()
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    for i in range(0,len(list2)):
        print ("Occurence of",list2[i],":",str.count(list2[i]))
n=input("Enter a string : ")
choice=1
while (choice==1):
    print ("\n******************MENU******************")
    print ("1.To display the word with longest length")
    print ("2.To determine the frequency of occurrence of particular character in the string")
    print ("3.To check whether given string is palindrome or not")
    print ("4.To display index of first appeareance of substring")
    print ("5.To count the occurrences of each word in the given string")
    ch=int(input("Enter your choice (From 1 to 5) : "))
    if (ch==1):
        print ("Longest word in the string is",longestword(n))
    elif (ch==2):
        freqofchar(n)
    elif (ch==3):
        palindrome(n)
    elif (ch==4):
        indexofsubstring(n)
    elif (ch==5):
        occurencesofword(n)
    else:
        print ("Invalid chocie")
    a=input("Do you want to continue (y/n) : ")
    if (a=='y'):
        choice=1
    else:
        choice=0
print("Thank you for using this program")
    
            
    

