# 44. Write a program to check traffic signal actions using match case.
signal = input("Enter signal color: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")