# Write a program to check exam results (Distinction, First Class, Pass, Fail).
marks = int(input("Enter the marks:"))
if marks >= 90:
    print("destinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else :
    print("Fail")            