#Write a program to check whether a triangle is equilateral, isosceles, or scalene.
a = int(input("Enter the first side  of triangle :"))
b = int(input("Enter the  second side of triangel:"))
c = int(input("Enter the third side of triangle"))
if a == b == c:
    print("equilateral triangle")
elif a == b or b == c or a == c:
    print("isosceles ")
else :
    print("scalence ")