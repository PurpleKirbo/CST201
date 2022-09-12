#this program uses a decison to determine the order of names 

#declare variables
fName1 = "" 
lName1 = ""
fName2 = "" 
lname2 = ""
name1 = ""
name2 = "" 

#prompt for names 
print("\t\tPlease enter the names of two students below")
fName1 = str(input("Enter the First name of student 1: "))
lname1 = str(input("Enter the Last Name for " + fName1 + ": "))

fName2 = str(input("Enter the First name of student 2: "))
lname2 = str(input("Enter the Last Name for " + fName2 + ": "))


#Processing 
name1 = fName1 + " " + lname1 
name2 = fName2 + " " + lname2 


#display the names in alphabetical order
print("\n\n\tThis is the names in aplhabetical order")
if (name1.upper() < name2.upper()):
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)     