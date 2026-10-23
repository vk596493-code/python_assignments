role = input("Enter role: ").lower()

match role:
    case "admin":
        print("Full Access")
    case "user":
        print("Limited Access")
    case "guest":
        print("Guest Access")
    case _:
        print("Invalid Role")
        