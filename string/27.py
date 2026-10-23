# 26. Find the first and last occurrence of a character.
s = input("Enter the string:")
ch = input("Enter the character:")

print("First occurrence:", s.find(ch))
print("Last occurrence:", s.rfind(ch))