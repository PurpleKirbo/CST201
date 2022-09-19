#This is a program for the Rock, Paper, Scissors Game

import random
from wsgiref.validate import InputWrapper 

#Declare Variables
computerNumber = 0 
userNumber = 0 

#Generate A random number for the computer
computerNumber = random.randint (0,2)

#prompt the user for rock paper or scissors
print("Please enter a Number in the Prompt, and do not leave empty")
print("\t\t\t(0) Scissors")
print("\t\t\t(1) Rock")
print("\t\t\t(2) Paper")
while True: 
    try:
        userNumber = int(input("\nPlease Enter your Choice from the menu above: "))
    except ValueError:
        print("\n\tYou did not enter a numeric Value!! Try again. ")
        continue
    else:
        break

print("\nThe computer number is: {0:d}".format (computerNumber)) 


#game code
if (computerNumber == 0): 
    if (userNumber == 0):
        print("\n\tThe Computer is scissors. You are scissors too. It is a draw.")
    elif (userNumber ==1): 
        print("\n\tThe Computer is scissors. You are Rock. You win!! :) ")
    elif (userNumber == 2):
        print("\n\tThe Computer is scissors. You Are Paper. You loose :( ") 
    else:
        print("\n\tYou did not enter a 0, 1 ,2. ")


if (computerNumber == 1): 
    if (userNumber == 0):
        print("\n\tThe Computer is rock. You are scissors. You Loose. :( ")
    elif (userNumber == 1): 
        print("\n\tThe Computer is Rock. You are Rock. It Is a draw. ")
    elif (userNumber == 2):
        print("\n\tThe Computer is Rock. You Are Paper. You Win! :) ") 
    else:
        print("\n\tYou did not enter a 0, 1 ,2. ")


if (computerNumber == 2): 
    if (userNumber == 0):
        print("\n\tThe Computer is Paper. You are scissors. You Win! :) ")
    elif (userNumber == 1): 
        print("\n\tThe Computer is Paper. You are Rock. You Loose :( ")
    elif (userNumber == 2):
        print("\n\tThe Computer is Paper. You Are Paper. It is a Draw. ") 
    else:
        print("\n\tYou did not enter a 0, 1 ,2. ")