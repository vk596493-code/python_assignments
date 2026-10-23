# 24. Extract only digits from a string.
s =input("Enter the character :")
digits=""
for ch in s:
    if ch.isdigit():
        digits+= ch
print(ch)        
