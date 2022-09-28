#This is a program for the Rock, Paper Scissor Game
import random

#Declare variables and initialize
computerNumber = 0
userNumber = 0
flag = "Y" 
while (flag.upper() == "Y"):

        #Generate a random number for the computer
        computerNumber = random.randint(0,2)

        #Prompt the user for scissors, Rock or Paper
        print("\n\nPlease enter a number below in the prompt, and do not leave empty")
        print("\t\t\t(0) Scissors")
        print("\t\t\t(1) Rock")
        print("\t\t\t(2) Paper")
        while True:
            try:
                userNumber = int(input("\nPlease enter your choice from the menu above: "))
            except ValueError:
                print("\n\tYou did not enter a numeric value!! Try again.")
                continue
            else:
                break
        print("\nThe computer number is: {0:d}".format(computerNumber))

        if (computerNumber == 0):
            if (userNumber == 0):
                print("\n\tThe computer is scissors. You are scissors  too. It is a draw.")
            elif (userNumber == 1):
                print("\n\tThe computer is scissors. You are rock. You win (-:")
            elif (userNumber == 2):
                print("\n\tThe computer is scissors. You are paper. You lose )-:")
            else:
                print("\n\tYou did not type in either a 0, 1 or 2!!")
        elif (computerNumber == 1):
            if (userNumber == 0):
                print("\n\tThe computer is rock. You are scissors. You lose )-:")
            elif (userNumber == 1):
                print("\n\tThe computer is rock. You are rock too. It is a draw.")
            elif (userNumber == 2):
                print("\n\tThe computer is rock. You are paper. You win (-:")
            else:
                print("\n\tYou did not type in either a 0, 1 or 2!!")
        elif (computerNumber == 2):
            if (userNumber == 0):
                print("\n\tThe computer is paper. You are scissors. You win (-:")
            elif (userNumber == 1):
                print("\n\tThe computer is paper. You are rock. You lose )-:")
            elif (userNumber == 2):
                print("\n\tThe computer is paper. You are paper. It is a draw.")
            else:
                print("\n\tYou did not type in either a 0, 1 or 2!!")    
        flag = str(input("\nIf you want to play again enter 'y' otherwise hit any other key to end the game"))      




















































































































































































#Start File Wednesday 9-28-22
