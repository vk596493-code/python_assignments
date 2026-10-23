month = int(input("Enter month number (1-12): "))
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
if 1 <= month <= 12:
    print("Month is:", months[month-1])
else:
    print("Invalid month number")
