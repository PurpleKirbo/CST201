#This program gets a test score and returns a letter grade

#Declare Variables and Initalize
score = 0.00
grade =  ""

#get input
score = float(input("Enter the grade for the student: "))

#Use a decsion to get the grade 
if (score >= 90):
    grade = "A"
elif((score >= 80) and (score < 90)):
    grade = "B"
elif((score >= 70) and (score < 80)): 
    grade = "C"
elif((score >= 60) and (score < 70)):
    grade = "D"
else: 
    grade = "F"

print("The letter grade for the score of {0:,.2f}: {1:s}".format(score, grade))                                     