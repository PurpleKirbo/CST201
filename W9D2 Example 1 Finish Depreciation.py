#This program is for displaying depreciation of a capital asset

def main():
    #Declare variables
    item = ""
    purYr = 0
    cost = 0.00
    numYrs = 0 #This will be our count loop control variable
    salvage = 0.00
    totalDep = 0.00
    slDep = 0.00
    beginValue = 0.00
    endValue = 0.00
    flag = "N" #This is our input validation condition loop control variable

    #Get Input
    print("\n\t*****DEPRECIATION PROGRAM FOR CAPITAL ASSET*****")
    while (flag.upper() == "N"): #This is our string input validation loop
        item = str(input("\nEnter the name of the capital asset: "))
        print("\n\tThe name of the asset you entered is: " + item)
        flag = str(input("\nIf this is not the correct name of the asset type 'n' or 'N'. Otherwise hit any other key: "))
    print("\n\tIn the prompt below make sure you only enter numeric data and do leave empty")
    while True:#This is the exception handling loop for input
        try:
            purYr = int(input("\nEnter the year of purchase for the captial asset: "))
            cost = float(input("Enter the origianl cost of the capital asset: $"))
            salvage = float(input("Enter the salvage value of the capital asset at the end of useful life: $"))
            numYrs= int(input("Enter the useful life of the capital asset (in whole years, such as 5): "))
        except ValueError:
            print("\n\tYou did not enter a numeric value for one or more of the numeric prompts. Try again!")
            continue
        else:
            break
        #this is the inital headings prior to out loop output
    print("\n\n{0:5s}{1:>12s}{2:>15s}{3:>18s}{4:>18s}".format("", "Beginning", "Amount of ", "Total  ", "Ending"))
    print("{0:5s}{1:>12s}{2:>15s}{3:>18s}{4:>18s}".format("Year", "Value ", "Depreciation", "Depreciation", "Value"))
    print("{0:5s}{1:>12s}{2:>15s}{3:>18s}{4:>18s}".format("----", "---------", "------------", "--------------", "------"))
    slDep = (cost-salvage)/numYrs #this is the calculation for straight line depreciation
    beginValue = cost #this will preserve he orginal cost variable while changeing the begging value in the loop
    #The following code is the for-loop for the depreciation schedule 
    for i in range (0, numYrs, 1):
        totalDep = totalDep + slDep #this updates total depreciation
        endValue = cost - totalDep #this updates the ending value variable 
        print("{0:5d}{1:>12,.2f}{2:>15,.2f}{3:>18,.2f}{4:>18,.2f}".format(purYr + i,beginValue,slDep,totalDep,endValue))
        beginValue = cost - totalDep #this will update the beggining value throught the loop
        

    print("\n\nThe total depreciation for the asset is: {0,.2f}".format(totalDep))
    print("The salvage value of the asset is cost ${o,.2f} minus total depreciation ${1:,.2f} which equals ${2:,.2f}".format(cost, totalDep, cost - totalDep))

        





main() #This calls the main function
















































































































































#Start file Wednesday 10-19-22
