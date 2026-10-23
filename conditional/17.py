marks = int(input("Enter the marks"))
if marks <0 or marks >100:
    print("invalid marks")
elif marks >=80:
    print("Grade A")
elif marks >=60:
    print("Grade B")
elif marks >=40:
    print("Grade C")
else:
    print("fail")
