#this program gets 3 test scores and displays their average
#it congradualates the user if the average is a high  score 


#Declare variables an initalize 
from cgi import test


test1 = 0.00
test2 = 0.00
test3 = 0.00
average = 0.00
fName = ""
lName = ""
name = ""

#constant
HIGHAVERAGE = 95


#get the names and  three test scores 
fName = str(input("Enter the first name of the student: "))
lName = str(input("Enter the last name of the student"))
name = fName + " " + lName 
print("\n\t***In the prompt below enter only numeric data and do not leave empty***")
test1 = float(input("Enter the score for" + name +  "for test 1: "))
test2 = float(input("Enter the score for" + name +  "for test 2: "))
test3 = float(input("Enter the score for" + name +  "for test 3: "))

#process average
average = (test1 + test2 + test3)/3

#print the average 
print("\n\n\tTEST DATA")
print("\t-------------")
print("the average test score for {0:s}: {1:,.2f}".format(name,average))

if (average >=HIGHAVERAGE):
    print("Congratulations, you have an above average test scores!")
else:
    print("You can work a little harder and get a average and get a average above the high of:" + str(format(HIGHAVERAGE, ',.1f')))    