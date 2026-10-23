#11. Count number of digits in a number.
n=int(input("Enter the number:"))
count = 0
while n >0:
    count+=1
    n//=10
print(count)
