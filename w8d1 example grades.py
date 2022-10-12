#this program is an example of a loop to enter student grades and get output for grades
#tis program also looks at input validation

def main():
    #declare Variables
    numOfStudents = 0
    total = 0.00
    count = 0 
    fName = ""
    lName = ""
    highStudent = ""
    student = ""
    highScore = ""
    score = 0.00
    average = 0.00
    hold = ""
    flag = 0 
    answer = "N"



    #input
    print("***In the prompt below enter numeric values and do not leave empty!***")
    while True:
        try:
            numOfStudents = int(input("\nEnter the number of students in the course: "))
        except ValueError:
                print("\n\tYou did not enter a numeric value. Please try again!")
        else: 
            break
    
    if (numOfStudents == 0):
        print("\n\tNo students were entered into the prompt for the course!")
    elif (numOfStudents < 0):
        print("\n\tThere cannot be a negative number of students in the course.")
    else:
        #start a for-loopback on the number of students in the course 
        for i in range(numOfStudents, 1):
            #below is a while loop fpr input vailidation of the name
            answer = "n" #thi resets the condition variable for the input vailidation within the for-loop
            while (answer.upper() == "N"): #this loop is for vailidation of the name which is a string
                #Strings do not return errors do you must vailidate these 
                fName = str(input("\nEnter student " + str(i + 1) + "'s first name: "))
                lName = str(input("Enter " + fName + "'s last name: "))
                student = fName + " " + lName
                print("\nt\t\tThe name you entered is:", student)
                answer = str(input("\nIf this is not the correct name enter n/N, else press any other key: "))
                if(answer.upper() == "N"):
                    print("\n\tEnter the name again below for the student " + str(i +1))
            while True:
                try:
                    score = float(input("\nEnter the grade for student " + str(student) + str(i + 1)))
                except ValueError:
                    print("\n\tYou did not enter a numeric value. Please try again!")
                    continue
                else:
                    break
            total = total + score #this keeps track of the total scores for all students
            count += 1 #this keeps track of the number of students (but this could also be the numOfStudents variable as well)
            if (score >= highScore):
                highScore = score
            if(i == (numOfStudents - 1)):
                hold = str(input("\n\******Press any key for final output********"))
            else:
                hold = str(input("\n\n********Press any key to continue******"))









main()