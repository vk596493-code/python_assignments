grade = input("Enter grade: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")