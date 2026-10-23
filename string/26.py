# 25. Extract only alphabets from a string.
s =input("Enter the string:")
alpha =""
for ch in s:
    if ch.isalpha():
        alpha +=ch
print(alpha)        