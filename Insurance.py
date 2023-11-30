# Program written to calculate One Stop Insurance's information for its customers.
# Date written: November 28th, 2023
# Author: Micheal Walsh

# Imports
from datetime import datetime, timedelta
# Define Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADDITIONAL_DISCOUNT = 0.25
LIABILITY_COVERAGE = 130.00
GLASS_COVERAGE = 86.00
CAR_LOAN_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_MONTHLY = 39.99

# Define required program functions

def insurancePremium(carTotal):
    insurancePaid = BASIC_PREMIUM
    if carTotal == 1:
        return insurancePaid
    if carTotal > 1:
        insurancePaid = BASIC_PREMIUM + carTotal * (BASIC_PREMIUM - (BASIC_PREMIUM * ADDITIONAL_DISCOUNT) )
        return insurancePaid

def calculateHST(untaxedAmt):
    float(untaxedAmt)
    taxedAmt = untaxedAmt + (untaxedAmt + (untaxedAmt * HST_RATE) )
    return taxedAmt

def formatDollars(unformattedAmt):
    float(unformattedAmt)
    formattedAmt = "${:,.2f}".format(unformattedAmt)
    return formattedAmt

# Gather Inputs
while True:

    while True: 
        firstName =input("Enter the customer's first Name: ").title()
        
        if firstName == "":
            print("Input cannot be blank - Please re-enter")
        else:
            firstName.title()
            break    

    while True:   
        lastName = input("Enter the customer's last name: ").title()

        if lastName == "":
            print("Input cannot be blank - Please re-enter")
        else:
            lastName.title()
            break

    while True:
        custAddress = input("Enter the customer's address: ")

        if custAddress == "":
            print("Input cannot be blank - Please re-enter")
        else:
            break

    while True:
        custCity = input("Enter the customer's city: ")

        if custCity == "":
            print("Input cannot be blank - Please re-enter")
        else:
            custCity.title()
            break

    while True:
        custProvince = input("Enter the customer's province: ")

        if custProvince.upper() in ["NL","PE","NS","NB","QC","ON","MB","SK","AB","BC","YT","NT","NU"]:
            break
        else:
            print("Input is wrong, check if blank or entered province is wrong.")
            
    while True:
        postCode = input("Enter the customer's postal code: ")

        if postCode == "":
            print("Input cannot be blank - Please re-enter")
        else:
            break

    while True:
        custPhoneNum = input("Enter the customer's phone number: ")

        if custPhoneNum == "":
            print("Input cannot be blank - Please re-enter")
        else:
            break

    while True:
        try:
            numCar = int(input("Enter the amount of cars being insured: "))
            break
        except ValueError:
            print("You have entered an invalid amount of cars, try again.")

    while True:
        extraLia = input("Would you like to add extra liability to these cars? (Y/N): ")

        if extraLia.upper() in ["Y","N"]:
            break
        else:
            print("Input is wrong, check if blank or entered data is wrong.")

    while True:
        glassCoverage = input("Would you like glass coverage? (Y/N): ")

        if glassCoverage.upper() in ["Y","N"]:
            break
        else:
            print("Input is wrong, check if blank or entered data is wrong.")

    while True:
        loanerCar = input("Would you like car loan coverage? (Y/N): ")

        if loanerCar.upper() in ["Y","N"]:
            break
        else:
            print("Input is wrong, check if blank or entered data is wrong.")

    while True:
        paymentOptions = input("How would you like to pay? Enter 'Full', 'Monthly' or 'Down Pay' to select your option: ").title()

        if paymentOptions == "Full":
            paymentSelection = "F"
            break
        if paymentOptions == "Monthly":
            paymentSelection = "M"
            break
        if paymentOptions == "Down Pay":
            paymentSelection = "D"
            downPayAmt = float(input("Enter how much you would like to put as down payment: "))
            break        
        else:
            print("Input is wrong, check if blank or entered data is wrong.")

    priceList = []
    dateList = []
    claimNum = 0
    while True:
        if claimNum == 3:
            break
        claimPrice = input("Enter the claim price (Enter END to continue, will also end if you enter 2 other claims): ")
        if claimPrice == "END":
            break
        claimDate = input("Enter the claim date (YYYY-MM-DD): ")
        claimNum +=1
        priceList.append(claimPrice)
        dateList.append(claimDate)

# Calculations

    insuranceAmt = insurancePremium(numCar)

    if extraLia == "Y":
        liabilityCost = numCar * LIABILITY_COVERAGE
        isExtraLia = "YES"
    else:
        liabilityCost = 0
        isExtraLia = "NO"

    if glassCoverage == "Y":
        glassCost = numCar * GLASS_COVERAGE
        isGlassCovered = "YES"
    else:
        glassCost = 0
        isGlassCovered = "NO"

    if loanerCar == "Y":
        loanCost = numCar * CAR_LOAN_COVERAGE
        isLoaning = "YES"
    else:
        loanCost = 0
        isLoaning = "NO"

    totalExtraCosts = glassCost + liabilityCost + loanCost
    totalInsurancePremium = insuranceAmt + totalExtraCosts

    totalCost = calculateHST(totalInsurancePremium)

    if paymentSelection == "F":
        payingAmt = totalCost
    elif paymentSelection == "M":
        payingAmt = (totalCost + PROCESSING_FEE_MONTHLY)/8
        monthlyPay = True
    elif paymentSelection == "D":
        payingAmt = ((totalCost - downPayAmt) + PROCESSING_FEE_MONTHLY)/8
        monthlyPay = True

    invoiceDateStr = datetime.now().strftime("%Y-%m-%d")
    firstPayDate = datetime(datetime.now().year, datetime.now().month + 1, 1).strftime("%Y-%m-%d")

    # Format dollar values

    insuranceAmtDSP = formatDollars(insuranceAmt)
    liabilityCostDSP = formatDollars(liabilityCost)
    glassCostDSP = formatDollars(glassCost)
    loanCostDSP = formatDollars(loanCost)
    totalExtraCostsDSP = formatDollars(totalExtraCosts)
    totalInsurancePremiumDSP = formatDollars(totalInsurancePremium)
    totalCostDSP = formatDollars(totalCost)
    payingAmtDSP = formatDollars(payingAmt)


    # Receipt

    print("One Stop Insurance Receipt")
    print("----------------------------------------")
    print(f"First Name: {firstName:>28s}")
    print(f"Last name: {lastName:>29s}")
    print(f"Address: {custAddress:>31s}")
    print(f"City: {custCity:>34s}")
    print(f"Province: {custProvince:>30s}")
    print(f"Postal Code: {postCode:>27s}")
    print(f"Phone Number: {custPhoneNum:>26s}")
    print(f"Number of Cars: {numCar:>24d}")
    print(f"Payment Option: {paymentOptions:>24s}")
    print("----------------------------------------")
    print("                  BILL                  ")
    print("----------------------------------------")
    print(f"Insurance Premium: {insuranceAmtDSP:>21s}")
    print(f"Extra Liability: {liabilityCostDSP:>23s}")
    print(f"Glass Insurance: {glassCostDSP:>23s}")
    print(f"Loaning Liability: {loanCostDSP:>21s}")
    print(f"Total Extra Costs: {totalExtraCostsDSP:>21s}")
    print(f"Total Insurance: {totalInsurancePremiumDSP:>23s}")
    print(f"Total Cost: {totalCostDSP:>28s}")
    if monthlyPay == False:
        print(f"Invoice Date: {invoiceDateStr:>26s}")
    if monthlyPay == True:
        print("----------------------------------------")
        print("            MONTHLY PAYMENTS            ")
        print("----------------------------------------")
        processingFeeDSP = formatDollars(PROCESSING_FEE_MONTHLY)
        print(f"Processing Fee: {processingFeeDSP:>24s}")
        if paymentOptions == "Down Pay":
            downPayAmtDSP = formatDollars(downPayAmt)
            print(f"Down Payment: {downPayAmtDSP:>26s}")
        print(f"Monthly Payment: {payingAmtDSP:>23s}")
        print(f"Invoice Date: {invoiceDateStr:>26s}")
        print(f"First Payment Date: {firstPayDate:>20s}")
    print("----------------------------------------")
    print("                 CLAIMS                 ")
    print("Claim #        Claim Date         Amount")
    print("----------------------------------------")
    print(f"{'1.':^10s} {dateList[0]:^20s} {'$'+priceList[0]:^10s}")
    print(f"{'2.':^10s} {dateList[1]:^20s} {'$'+priceList[1]:^10s}")
    print(f"{'3.':^10s} {dateList[2]:^20s} {'$'+priceList[2]:^10s}")
    while True:
        Continue = input("Would you like to repeat the program? (Y / N): ").upper()

        if Continue != "Y" and Continue != "N":
            print("Y or N must be entered")
        else:
            break
    
    if Continue == "N":
        break
