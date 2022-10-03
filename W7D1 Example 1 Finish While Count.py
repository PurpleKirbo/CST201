#This is an example of a while loop
def main():
    #Declclare variables and initialize
    countPositive = 0
    countNegative = 0
    count = 0
    total = 0
    num = 0 #This will be the while loop flag
    highest = 0
    num = int(input("Enter a integer number (type '0' to end calculations): "))#Priming read
    highest = num #Set the highest variable to the first number entered
    while (num != 0):
        if (num > 0):
            countPositive = countPositive + 1
        elif (num < 0):
            countNegative += 1 #This is a shortcut for "countNegative = countNegative + 1"
        #Below keeps a total of all numbers
        total = total + num #Shortcut for this would be "total += num"
        #Below keeps track of how many numbers entered
        count += 1 #This could be "count = count + 1"
        if (num > highest):#This decision will keep track of the highest number entered
            highest = num
        #Below ask for another number or to end the loop
        num = int(input("\nEnter a integer number (type '0' to end calculations): "))
    #The loop has ended and we have output
    if (count == 0):
        print("\n\tNo numbers were entered!")
    else:
        print("\n\n\t\t\tOUTPUT")
        print("\t\t\t------")
        print("The number of positive numbers entered is: {0:,d}".format(countPositive))
        print("The number of negative numbers entered is: {0:,d}".format(countNegative))
        print("The total value of the integers entered is:", format(total, ',d'))
        print("The average of the integers entered: {0:,.3f}".format(total/count))
        print("The highest number entered is: {o:,d}".format(highest))

main()























































































































#Start file for Monday 10-3-22





    
