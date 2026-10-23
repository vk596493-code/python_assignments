num1 = int(input("Enter the  first number"))
num2 = int(input("Enter the second number:"))
if num1 % 2!=0:
    num1 +=1
for i in range(num1,num2+1,2):
    print(i)