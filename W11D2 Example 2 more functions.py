#this program will calculate a bonus using functions
#Declare global variables
CONTRIBUTIONRATE = 0.05


def main():
    #declare local variables
    grossPay = 0.00
    bonus = 0.00
    totalContribution = 0.00
    contribution = 0.00
    grossPay, bonus = GetInput(grossPay, bonus)
    contribution = ShowPayContribution(grossPay, contribution)
    totalContribution = CalculateContribution(totalContribution, contribution)
    ShowBonusContribution(bonus, totalContribution)

def GetInput(gp, b):













main()