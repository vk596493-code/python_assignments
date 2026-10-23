#5. Count the number of consonants in a string.
s =input("Enter the string:")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
print("Consonants:", sum(1 for ch in s if ch in consonants))