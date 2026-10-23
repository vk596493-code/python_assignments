# 37. Find the longest word in a sentence.
s = input("Enter sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)