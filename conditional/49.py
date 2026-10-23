result = input("Enter result (pass/fail): ").lower()

match result:
    case "pass":
        print("Congratulations! You Passed.")
    case "fail":
        print("Better Luck Next Time.")
    case _:
        print("Invalid Result")