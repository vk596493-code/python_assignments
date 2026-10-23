choice = int(input("""
1. Balance Enquiry
2. Withdraw
3. Deposit
4. Exit

Enter your choice: """))

match choice:
    case 1:
        print("Balance: Rs. 10,000")
    case 2:
        print("Withdrawal Successful")
    case 3:
        print("Deposit Successful")
    case 4:
        print("Thank You for Visiting")
    case _:
        print("Invalid Choice")