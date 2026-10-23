# 38. Find the shortest word in a sentence.
s = input("Enter sentence: ")
words = s.split()
shortest = min(words, key=len)
print("Shortest word:", shortest)