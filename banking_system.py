# Author: Wiktor Kubasiak
# Student Number: R00162970
# Title: Modular Programming - Project
# Project Title: Banking System 

import random  # This module will be used to generate a random 5 digit number for a new bank account number.
import math  # This module will be used to calculate the largest amount on deposit in the bank.

bank_details = []  # I am creating a blank list which will hold all bank details contained in bank.txt file.

bank_account_numbers = []  # I am creating a blank list that will contain all account numbers.
bank_account_balances = []  # I am creating a blank list that will contain all account balances.
bank_account_names = []  # I am creating a blank list that will contain all account names.


def read_data_from_file_into_lists():
    file_to_read = open("bank.txt", 'r')  # I am opening the file bank.txt in read only mode.
    try:  # I am making sure that all indented instructions will work as expected.
        for line in file_to_read:
            bank_details.append(line.strip())  # strip() will remove unseen new line character after each line
    finally:
        file_to_read.close()  # At the end I am closing the file to be read.

    """                       
    In the for loop I am appending account number, account balance
    and account name as one element in the list with spaces for each list index.

    Sample output:
    ['58697 3233.99 Michael Murphy', '17200 1500.00 Wiktor Kubasiak', '61307 750.00 Piotr Skoczylas',
     '19075 10000.00 Mike Wazowski', '11579 25.00 Karol Padlewski']

    The file format which I chose:

    98768 8077.00 Jim McIntyre
    58697 23233.99 Michael Murphy
    35318 4545.12 Abigail Buckley                                            
    20454 23233.45 Marie Delaney                                                                                                                                   
    """

    for line in bank_details:
        line_list = line.split()  # split() enables me to divide every single line
        bank_account_numbers.append(line_list[0])  # I am assigning account number by index (first column)
        bank_account_balances.append(float(line_list[1]))  # I am assigning account balance by index (second column)
        bank_account_names.append(line_list[2] + " " + line_list[3])

        """
        I am assigning account name by index
        (third and fourth column) with a space
        between first name and surname.
        """

    """
    In the for loop I am splitting each line to columns by indexes so that I will be able to assign account numbers,
    account balances and account names to separate lists.

    Sample output:
    ['58697', '17200', '61307', '19075', '11579']
    [3233.99, 1500.0, 750.0, 10000.0, 25.0]
    ['Michael Murphy', 'Wiktor Kubasiak', 'Piotr Skoczylas', 'Mike Wazowski', 'Karol Padlewski']
    """


read_data_from_file_into_lists()


def main_menu():
    try:  # I am giving user a try.
        user_choice = int(input("*****************************************************************"
                                "\n1: Open an account"
                                "\n2: Close an account"
                                "\n3: Withdraw money"
                                "\n4: Deposit money"
                                "\n5: Generate a report for management"
                                "\n6: Quit"
                                "\n>>> "))  # I am giving user a choice related to functionality.

        while user_choice < 1 or user_choice > 6:  # I am ensuring that the user will enter a value between 1 and 6.
            print("Invalid input, please choose one of the following options:")
            user_choice = int(input("1: Open an account"
                                    "\n2: Close an account"
                                    "\n3: Withdraw money"
                                    "\n4: Deposit money"
                                    "\n5: Generate a report for management"
                                    "\n6: Quit"
                                    "\n>>> "))

        if user_choice == 1:
            open_an_account()
        elif user_choice == 2:
            close_an_account()
        elif user_choice == 3:
            withdraw_money()
        elif user_choice == 4:
            deposit_money()
        elif user_choice == 5:
            generate_a_report_for_management()
        elif user_choice == 6:
            quit_program_and_write_lists_into_file()

        # Based on the option chosen the user will have an opportunity to avail of the program's functionality.

    except ValueError:
        print("An error has occurred, please run the program again entering correct values.")

    # If something goes wrong and the user types anything different than a number, the above message will be displayed.


def open_an_account():
    new_account_number = random.randint(00000, 99999)  # I am generating a random 5 digit number.
    while new_account_number in bank_account_numbers:
        random.randint(00000, 99999)

    # I am ensuring that it will be a new, unique account number.

    bank_account_numbers.append(str(new_account_number))  # I am adding new account number to the list.

    current_balance = 0  # Bank account balance will always be zero when opening a new account.
    bank_account_balances.append(current_balance)  # I am adding account balance to the list.

    full_name = input("Please enter your full name >>> ")  # I am asking user for the full name.
    while full_name in bank_account_names:
        full_name = input("This name already exists in the database, please enter different name >>> ")

    # I am ensuring that the name does not already exist in the database(file).

    bank_account_names.append(full_name)  # I am adding full name to the list.

    print("Your full name:", full_name)
    print("Your new account number:", new_account_number)
    print("Your current balance:", current_balance)

    # I am displaying information for the user.

    main_menu()


def close_an_account():
    account_number = input("Please enter your account number >>> ")  # I am asking the user for existing account number.
    while account_number not in bank_account_numbers:
        account_number = (input("This account number does not exist in the database, try again >>> "))
        if account_number not in bank_account_numbers:
            question = input("This account number does not exist in the database, do you want to quit? (y/n) ")
            while question != "y" and question != "n":
                question = input("Do you want to quit (y/n) ")
            if question == "y":
                break

    """
    In the while loop I am verifying if account number exists in the database(file). If the user still provides
    incorrect information I keep asking about it until the user chooses to quit by inserting '(y/n)'. If the answer
    is not 'y' or 'n' another while loop will be asking forever. If the user types 'y' it will exit the loop or keep
    asking otherwise.
    """

    if account_number in bank_account_numbers:
        position_in_the_list = bank_account_numbers.index(account_number)  # I am setting a linkage to account number.
        bank_account_numbers.remove(account_number)  # I am removing determined account number from the database.
        del bank_account_balances[position_in_the_list]  # I am deleting balance associated with the account number.
        del bank_account_names[position_in_the_list]  # I am deleting name associated with the account number.

    # If the account number is indeed in the database(file) it will delete all data associated with it.

    main_menu()


def withdraw_money():
    account_number = input("Please enter your account number >>> ")  # I am searching for a bank account by its number.
    while account_number not in bank_account_numbers:
        account_number = (input("This account number does not exist in the database, try again >>> "))
        if account_number not in bank_account_numbers:
            question = input("This account number does not exist in the database, do you want to quit? (y/n) ")
            while question != "y" and question != "n":
                question = input("Do you want to quit (y/n) ")
            if question == "y":
                break

    """
    As it was in the 'close_an_account' function the while loop verifies if account number exists in the database(file).
    If the user still provides incorrect information I keep asking about it until the user chooses to quit by inserting
    '(y/n)'. If the answer is not 'y' or 'n' another while loop will be asking forever. If the user types 'y' it will
    exit the loop or keep asking otherwise.
    """

    if account_number in bank_account_numbers:  # If account number is in the database(file), set the conditions ...
        position_in_the_list = bank_account_numbers.index(account_number)  # I am setting a linkage to account number.
        amount_of_money = float(input("Enter the amount that you would like to withdraw >>> "))
        # I am asking about the amount which the user wants to withdraw.
        while amount_of_money > bank_account_balances[position_in_the_list]:
            amount_of_money = float(input("You have insufficient funds on your account, enter a smaller amount >>> "))
            if amount_of_money > bank_account_balances[position_in_the_list]:
                question = input("You have insufficient funds on your account, do you want to quit (y/n) ")
                while question != "y" and question != "n":
                    question = input("Do you want to quit (y/n) ")
                if question == "y":
                    break

        """
        In the above while loop I am verifying if the user has got enough funds on the account. If the user still
        provides an amount that is too high, I am suggesting a smaller amount. If the amount is constantly too high
        I keep asking about it until the user chooses to quit by inserting '(y/n)'. If the answer is not 'y' or 'n'
        another while loop will be asking forever. If the user types 'y' it will exit the loop or keep asking otherwise.
        """

        if amount_of_money <= bank_account_balances[position_in_the_list]:
            bank_account_balances[position_in_the_list] = bank_account_balances[position_in_the_list] - amount_of_money
            print("You have", "€" + format(bank_account_balances[position_in_the_list], '.2f'), "on your account now.")

        # If the user has indeed got enough funds, it will withdraw the specified amount and display the balance.

    main_menu()


def deposit_money():
    account_number = input("Please enter your account number >>> ")  # I am searching for a bank account by its number.
    while account_number not in bank_account_numbers:
        account_number = (input("This account number does not exist in the database, try again >>> "))
        if account_number not in bank_account_numbers:
            question = input("This account number does not exist in the database, do you want to quit? (y/n) ")
            while question != "y" and question != "n":
                question = input("Do you want to quit (y/n) ")
            if question == "y":
                break

    """
    As in the previous two functions the while loop verifies if account number exists in the database(file).
    If the user still provides incorrect information I keep asking about it until the user chooses to quit by inserting
    '(y/n)'. If the answer is not 'y' or 'n' another while loop will be asking forever. If the user types 'y' it will
    exit the loop or keep asking otherwise.
    """

    if account_number in bank_account_numbers:
        position_in_the_list = bank_account_numbers.index(account_number)  # Establish a linkage to account number.
        amount_of_money = float(input("Enter the amount which you would like to deposit >>> "))
        # Ask about the amount of money which the user would like to deposit.
        bank_account_balances[position_in_the_list] = bank_account_balances[position_in_the_list] + amount_of_money
        print("You have", "€" + format(bank_account_balances[position_in_the_list], '.2f'), "on your account now.")

    """
    If the account number is indeed in the database(file), deposit a user-specified amount of money
    and display the current balance for the user's own record.
    """

    main_menu()


def generate_a_report_for_management():
    print(format("Account name", '20s'), format("Account number", '20s'), format("Account balance", '15s'))
    # Display 'Account name', 'Account number' and 'Account balance' with a field of 20, 20 and 15 spaces.
    print("-" * 65)  # Form some sort of a table.

    for account_name in bank_account_names:
        position_in_the_row = bank_account_names.index(account_name)  # Set a linkage to bank account name.
        print(format(account_name, '21s'), format(bank_account_numbers[position_in_the_row], '21s'), format("€", "1s"),
              format(bank_account_balances[position_in_the_row], '3.2f'), sep="")

    """
    In the above for loop I am creating a table with the details of all accounts:
    account name with a field of 21 spaces, account number related to it with a field of 21 spaces,
    a € symbol with a single space, account balance related to account name with a field of 3 spaces,
    all of them with no separation(sep="").
    """

    total_deposit = 0  # Deposit counter is 0 at the start.
    largest_amount_on_deposit = -math.inf
    # I am referring to the math module, the first amount will be the largest and then it can change.
    name_with_largest_amount_on_deposit = ""  # This variable will hold the account holder with largest balance.

    for balance in bank_account_balances:
        account_holder_link = bank_account_balances.index(balance)  # Establish a linkage to the account holder.
        if balance > largest_amount_on_deposit:
            largest_amount_on_deposit = balance
            name_with_largest_amount_on_deposit = bank_account_names[account_holder_link]
        total_deposit += balance

    """
    In the for loop I am calculating the largest amount on deposit specifying the account holder and the total
    amount on deposit in the bank iterating through the list of balances.
    """

    print("-" * 65)  # Finish forming the table here.
    print("Total amount on deposit in the bank: €", format(total_deposit, '.2f'), sep="")
    print("The largest amount on deposit amounts to", "€" + format(largest_amount_on_deposit, '.2f'), "held by",
          name_with_largest_amount_on_deposit + ".")

    # Display the statistics: total deposit and largest amount on deposit to 2 decimal places.

    main_menu()


def quit_program_and_write_lists_into_file():
    output_file = open("bank.txt", 'w')  # I am opening the file bank.txt in write mode.

    for account_number in bank_account_numbers:
        position_in_the_row = bank_account_numbers.index(account_number)  # I am setting a linkage to account number.
        output_file.writelines(account_number + " " + str(format(bank_account_balances[position_in_the_row], '.2f') +
                                                          " " + (bank_account_names[position_in_the_row]) + "\n"))

        # Write out account number, associated balance to 2 decimal places and associated name.

    """
    In the for loop I am writing out the data from the lists back to bank.txt file in the original form as
    it was at the beginning.
    """

    output_file.close()  # I am closing the file bank.txt .

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Thank you for using my software.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Some graphical ornament and valediction towards the user.

    exit()  # I am terminating the program at this stage.


main_menu()
