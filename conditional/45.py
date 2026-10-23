choice = int(input("1.Idli\n2.Dosa\n3.Puri\nEnter choice: "))

match choice:
    case 1:
        print("You selected Idli")
    case 2:
        print("You selected Dosa")
    case 3:
        print("You selected Puri")
    case _:
        print("Invalid Choice")