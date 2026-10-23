#4. Count the number of vowels in a string.
s  = input("Enter the string:")
vowels = "aeiouAEIOU"
print("vowels:",sum(1 for ch in s  if ch in vowels))
