a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+,-,*,/): ")

match op:
    case "+": print("Result =", a+b)
    case "-": print("Result =", a-b)
    case "*": print("Result =", a*b)
    case "/": print("Result =", a/b if b!=0 else "Division by zero error")
    case _: print("Invalid operation")
