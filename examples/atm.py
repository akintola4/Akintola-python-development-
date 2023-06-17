print("WELCOME TO THE BANK OF AMERICA")
account = int(input("enter your account number: "))
pin = int(input("enter your PIN: "))

if (pin <= 999 or pin >= 9999):
    print("invaild password")
else:
    balance = 200000
    print("1 for Balance")
    print("2 for Deposit")
    print("3 for Withdraw")
    print("4 for Transfer")
    print("5 for Top Up")
    option = int(input("enter your choice: "))
    
    if (option == 1):
        # this will show the balance in the account
        print("your balance is: ", balance)
    elif (option == 2):
        # this will allow the user to deposit
        deposite = int(input("enter the amount of cash you wish to deoposit with us today: "))
        balance += deposite
        print("Deposite was SUCCESSFUL and your new balance is: ", balance)
    elif (option == 3):
        # this will allow the user the withdraw cash from the his account
        withdraw = int(input("enter the amount of cash you wish to withdraw from us today: "))
        balance -= withdraw
        print("withdraw was successful and your new balance is: ", balance)
    elif (option == 4):
        # this will allow us transfer our casb to another account 
        transferId = int(input("enter the account number of the person you wish to transfer to: "))
        transferAmount = int(input("enter the amount of cash you wish to transfer:  "))
        balance -= transferAmount
        print(f"you have successfullt transfered" , transferAmount , "to account number: " , transferId)
        print("your remain balance is: ", balance)
    elif (option == 5):
        # this will allow us top up our phone number with cash 
        phoneId = int(input("enter the phone number of the person you wish to credit to: "))
        creditAmount = int(input("enter the amount of cash you wish to pay for the credit:  "))
        balance -= creditAmount
        print(f"you have successfullt transfered" , creditAmount , "to account number: " , phoneId)
        print("your remain balance is: ", balance)