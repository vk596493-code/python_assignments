# 23. Check whether a string is a palindrome.
s =input("Enter the string:")
if s==s[::-1]:
    print("Palindrome")
else:
    print("not palindrome")    