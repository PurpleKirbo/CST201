#this program determines whether a band customer qualifies for a loan

#declare variables
salary = 0.00
yearsOnJob = 0 

#constnats
MINSALARY = 30000.0 #This is minimum salary to qualify for a load
MINYEARS = 2 #this is minimum years to be employed to qualifiy for a loan 


#get input
salary = float(input("Enter the annual salary of the load applicant: $"))
yearsOnJob = int(input("Enter the loan applicants number of years employed: "))

#determine of the applicant qualifies for the loan
if (salary >= MINSALARY):
    if (yearsOnJob >= MINYEARS):
        print("You Qualify for the loan!! Great")
    else:
        print("You have the minimum salary but you do not meet the requirements for the employment!")
else: 
    if (yearsOnJob >= MINYEARS):
        print("You have the minimum years of employment for a loan but do not meet te salary requirements!")   
    else:
        print("You do not meet either the minium years of employment or the salary requirements for the loan!")             
