# Author: Wiktor Kubasiak
# Student Number: R00162970
# Title: Programming Fundamentals - Project
# Project Title: Booking System

try:  # I am having a try.

    # Group's manager details
    nameOfManager = input("Please enter your full name>>> ")
    emailOfManager = input("Please enter your email address>>> ")
    numberOfManager = input("Please enter your phone number>>> ")

    # Starting date
    startingDate = input("What is the starting date you are looking for? (DD/MM/YYYY)>>> ")

    # Band's details & Time period
    numberOfMembers = int(input("How many members of the band do you want to accommodate? "))
    numberOfDays = int(input("For how many days? "))

    bandMembers = ""   # This variable is used as an accumulator.

    for member in range(numberOfMembers):
        nameOfMember = input("What is band member #" + str(member + 1) + "'s name? ")
        nameOfInstrument = input("What is " + str(nameOfMember) + "'s instrument? ")
        bandMembers += str(member + 1) + ". " + nameOfMember + " - " + nameOfInstrument + "\n"

    '''
    In the above for loop I am asking for each member and its instrument individually based on the number of members
    entered by user.
    str(member + 1) = which member in turn, converted to a string
    str(nameOfMember) = name of particular member, converted to a string
    In the last line of the for loop I am accumulating each member in turn with its instrument to an empty string.
    '''

    # Available room & Sessions
    maximumNumberOfSpaces = 8
    availableRoom = maximumNumberOfSpaces - numberOfMembers
    print("There is room for", availableRoom, "session musicians.")
    numberOfSessions = int(input("How many sessions will you need? "))

    # I am calculating the available room and I am asking how many sessions will be needed.

    while numberOfSessions > availableRoom:
        print("The number of sessions cannot be greater than the available room for session musicians.")
        numberOfSessions = int(input("Please enter the correct amount>>> "))

    '''
    In the above while loop I am ensuring that the number of sessions will not exceed the available room.
    The programme will be asking the user about the amount until he/she enters the correct amount.
    '''

    # Payment method & Charges
    pricePerSession = 100
    priceForStudioDaily = 260
    creditCardLevy = 0.05
    cashDiscount = 0.05

    if numberOfDays == 1:
        priceForStudioDaily = priceForStudioDaily
    elif 2 <= numberOfDays <= 4:
        priceForStudioDaily = priceForStudioDaily - 20
    elif 5 <= numberOfDays <= 8:
        priceForStudioDaily = priceForStudioDaily - 50
    elif numberOfDays > 8:
        priceForStudioDaily = priceForStudioDaily - 60

    # I am establishing the price for the rent of studio given the number of days entered by the user.

    totalCost = pricePerSession * numberOfSessions * numberOfDays + priceForStudioDaily * numberOfDays

    # I am giving Python formula to calculate the total price which the group's manager will have to pay.

    paymentMethod = input("Which payment method will you use? "
                          "\n1: Credit card (5% levy)"
                          "\n2: Cash (5% discount)"
                          "\n3: Cheque"
                          "\n>>>")

    # I am giving the user a choice in regard to the payment methods in a menu format.

    if paymentMethod == "1":
        totalCost = totalCost + totalCost * creditCardLevy
        paymentMethod = "credit card"
    elif paymentMethod == "2":
        totalCost = totalCost - totalCost * cashDiscount
        paymentMethod = "cash"
    elif paymentMethod == "3":
        totalCost = totalCost
        paymentMethod = "cheque"

    # The total price will differ depending on the user's choice made.

    # Information for the user
    print("Booking application")
    print("-------------------")
    print("Requested by:", nameOfManager, "( Contact:", emailOfManager, "&", numberOfManager, ")")

    print("\nDate requested >>>", startingDate)

    print("\nBand Members")
    print("------------")
    print(bandMembers)

    print("It includes", numberOfSessions, "session musicians per day.")
    print("Payment will amount to", totalCost, "€ to be paid by", paymentMethod + ".")

    print("\nThank you for using my program.")

    # Information for the user which will be written to a txt file.
    outputFile = open("Request.txt", 'w')

    outputFile.write("Booking application\n-------------------")
    outputFile.write("\nRequested by: " + nameOfManager + " ( Contact: " + emailOfManager + " & " + numberOfManager
                                                                                                  + " )")
    outputFile.write("\n\nDate requested >>> " + startingDate)
    outputFile.write("\n\nBand Members\n------------" + "\n" + bandMembers)
    outputFile.write("\nIt includes " + str(numberOfSessions) + " session musicians per day.")
    outputFile.write("\nPayment will amount to " + str(totalCost) + " € to be paid by " + paymentMethod + ".")
    outputFile.write("\n\nThank you for using my program.")

    outputFile.close()

except ValueError:   # I am raising an exception which will handle possible error related with user input.
    print("You have entered an incorrect value, please run the program again.")
