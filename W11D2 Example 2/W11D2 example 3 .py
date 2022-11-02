#this program sets up a menu to allow users to manipulate a bank account



def main():
    #declare local variables
    selection = 0
    balance = 0.00
    flag = 0 
    while (flag == 0):
        selection = MainMenu(selection)
        if (selection == 1):
            balance = Deposit(balance)
            continue
        elif (selection == 2):
            balance = Withdrawal(balance)
            continue
        elif (selection == 3):
            ShowBalance(balance)
            continue
        elif (selection == 4):
            print("\n\t\tThank you for banking with us!")
            flag = 1
        else:
            print("\n\n\t\tInvaild Choice! Choices are 1 - 4")
            MainMenu(selection)
            continue


def MainMenu(sel):
    #this function shows the main menu for a bank program
    sel = 0 
    print("{0:40s}{1:30s}".format("", "MILLER BANK"))
    print("{0:20s}{1:50s}".format("", "**********************************************"))
    print("{0:20s}{1:50s}".format("", "---PLEASE MAKE A SELECTION FROM THE MENU BELOW"))
    print("{0:20s}{1:50s}".format("", "**********************************************"))
    print("\n{0:35s}{1:35s}".format("", "(1) Make Deposit"))
    print("\n{0:35s}{1:35s}".format("", "(2) Make Withdrawal"))
    print("\n{0:35s}{1:35s}".format("", "(3) Show Balance"))
    print("\n{0:35s}{1:35s}".format("", "(4) "Exit Program"))
    sel = int(input("\nEnter a Selection: "))
    return sel 



main()
