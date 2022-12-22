print("-----Program for Student Information-----")
 
D = dict()
 
n = int(input('How many student record you want to store : '))
 
# Add student information
# to the dictionary
for i in range(0,n):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    z = input("Enter contact number: ")
    m = input('Enter Marks: ')
    l = input('Enter roll number: ')
    D[x, y] = (z, m, l)


def display(roll):
    print("\n-----DETAILS------\n")
    flag=0
    for key in D:
        
        tup=D[key]
        if(roll == tup[2]):
            flag=1
            
            print("First Name: ",key[0])
            print("Last Name: ",key[1])
            
            print("Contact Number: ",tup[0])
            print("Marks: ",tup[1])
            print("Roll number: ",tup[2])
    if(flag==0):
        print("Roll number doesn't exist!! ")

     
# define a function for shorting
# names based on first name
def sort():
    ls = list()
    # fetch key and value using
    # items() method
    for sname,details in D.items():
       
        # store key parts as an tuple
        tup = (sname[0],sname[1])
         
        # add tuple to the list
        ls.append(tup)   
         
    # sort the final list of tuples
    ls = sorted(ls)   
    for i in ls:
       
        # print first name and second name
        print(i[0],i[1])
    return


   
# define a function for
# finding the minimum marks
# in stored data
def minmarks():
    ls = list()
    # fetch key and value using
    # items() methods
    for sname,details in D.items():
        # add details second element
        # (marks) to the list
        ls.append(details[1])   
     
    # sort the list elements   
    ls = sorted(ls)   
    print("Minimum marks: ", min(ls))
     
    return
   
# define a function for searching
# student contact number
def searchdetail(fname):
    ls = list()
     
    for sname,details in D.items():
       
        tup=(sname,details)
        ls.append(tup)
         
    for i in ls:
        if i[0][0] == fname:
            print(i[1][0])
    return
   
# define a function for
# asking the options
def option():
   
    choice = int(input('Enter the operation detail: \n \
    1: Sorting using first name \n \
    2: Finding Minimum marks \n \
    3: Search contact number using first name: \n \
    4: Search details of student with roll number: \n \
    5: Exit\n \
    Option: '
    ))
    
     
    if choice == 1:
        # function call
        sort()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()


             
        # exit function call   
        exit()
         
    elif choice == 2:
        minmarks()
        print('Want to perform some other operation??? Y or N: ')
         
        inp = input()
        if inp == 'Y':
            option()
        exit()
         
    elif choice == 3:
        first = input('Enter first name of the student: ')
        searchdetail(first)
         
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()
             
        exit()
    elif choice == 4:
        rollnumber = input('Enter roll number of student: ')
        print(" ")
        display(rollnumber)
        
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()
        else:
            print('Thanks for executing me!!!!')
            exit()
         
option()
