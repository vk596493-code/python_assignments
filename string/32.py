# 31. Remove punctuation marks from a string.
import string
s =input("Enter the string:")

for ch in string.punctuation:
    s.replace(ch,"")
print(s)    
