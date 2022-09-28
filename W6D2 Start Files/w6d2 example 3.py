#this is a example of a while loop
def main():
    #Declare variables and initalize
    countPositive = 0 
    countNegative = 0 
    count = 0 
    total = 0 
    num = 0 #this will be the while loop flag
    highest = 0 
    num = int(input("Enter a integer number, (type '0' to end calculations): ")) #priming read
    highest = num #Set the highest variable to the first number entered 
    while (num != 0):
        if(num > 0):
            countPositive = countPositive + 1 
        elif (num < 0):
            countNegative += 1  #This is a shortcut 
        #Below keeps a total of all numbers
        total = total + num #shortcut would be += 
        #Below keeps track of how many numbers entered
        count += 1 #could be count = count + 1 
        if (num > highest): #this decsion will keep  track of the giest number entered 
            highest = num 
        #below ask for another number or end the loop
    num = int(input("\nEnter a integer number (type '0' to end calculations): "))
#the loop has ended and we have output
if (count == 0):
    print("\n\tNo Numbers were Entered!")
else:
    print("\n\n\n\t\tOUTPUT")
    print("\t\t\t----------")
    print("The number of positive numbers entered is: {0:,d}".format(countPositive))
    print("The number of negative numbers entered is: {0:,d}".format(countNegative))