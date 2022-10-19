#This program is an example of a for loop to enter student grades and get output for grades
#This program also looks at input validation
def main():
    #Declare variables and initialize
    numOfStudents = 0
    total = 0.00
    count = 0
    fName = ""
    lName = ""
    student = "" #This variable is used to concatenate the first name and last name
    highScore = 0.00
    score = 0.00
    average = 0.00
    hold = ""
    flag = 0
    answer = "N" #This variable is used to control the input validation for the name
    output = "" #We are going to use this variable to 
    #input
    print("****In the prompt below only enter numeric values and do not leave empty****")
    while True:
        try:
            numOfStudents = int(input("\nEnter the number of students in the course: "))
        except ValueError:
            print("\n\tYou did not enter a numeric value. Try again!")
            continue
        else:
            break
    if (numOfStudents == 0):
        print("\n\tNo students were entered into the prompt for the course!")
    elif (numOfStudents < 0):
        print("\n\tThere cannot be a negative number of students in a course")
    else:
        #Start a for-loop based on the number of students in the course
        for i in range(0,numOfStudents,1):
            #Below is a while loop for input validation of the name
            answer = "N" #This resets the condition variable for the input validation within for-loop
            while (answer.upper() == "N"):#This loop is for validation of the name which is a string
                #Strings do not throw exceptions. So you must validate within a loop 
            
                fName = str(input("\nEnter student " + str(i + 1) + "'s first name: "))
                lName = str(input("Enter " + fName + "'s last name: "))
                student = fName + " " + lName
                print("\n\t\tThe name you entered is:", student)
                answer = str(input("\nIf this is not the correct name enter n/N, else press any other key: "))
                if(answer.upper() == "N"):
                    print("\n\tEnter the name again below for student " + str(i + 1))
            while True:
                try:
                    score = float(input("\nEnter the grade for student " + str(student) + ": "))
                except ValueError:
                    print("\n\tYou did not enter a numeric value. Try again!")
                    continue
                else:
                    break
            total = total + score #This keeps track of the total scores for all students
            count += 1 #This keeps track of the number of students (but this should also be in the numOfStudent variable)
            #we could add the student and the grade to a list or a file at this point
            #then, use a loop in final output, to loop through the list ir file to show all students and their grade in the course 
            output = "\t" + student + "\t" + str(format(score, ',.2f'))
            if (score > highScore):
                highScore = score
            if(i == (numOfStudents - 1)):
                hold = str(input("\n\n*****Press any key for final output****"))
            else:
                hold = str(input("\n\n*****Press any key to continue"))
        
        #below will start final output
        print("\n\n\tSTUDENT NAME\tGRADE")
        print("\t-----------\t---------\n")
        print(output)
        print("\n\nThe average grade for all students is: {0:,.2f}".format(total/count))
        print("The highest score for the course is: {0:,.2f}".format(highScore))
                
                
                

main() #This calls (starts) the main function





























































































































































































#Start file Monday 10/17/22

