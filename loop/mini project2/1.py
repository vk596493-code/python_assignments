def text_analyzer(text):
    text = " ".join(text.split())

    char_count = len(text)
    word_count = len(text.split()) 
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"

    v_count = c_count = d_count = s_count = 0
    for ch in text:
        if ch in vowels:
            v_count += 1
        elif ch in consonants:
            c_count += 1
        elif ch in digits:
            d_count += 1
        elif not ch.isspace():
            s_count += 1

    upper_text = text.upper()
    lower_text = text.lower()

    freq = {}
    for w in text.split():
        freq[w] = freq.get(w, 0) + 1

    print("Characters:", char_count)
    print("Words:", word_count)
    print("Sentences:", sentence_count)
    print("Vowels:", v_count, "Consonants:", c_count)
    print("Digits:", d_count, "Special Characters:", s_count)
    print("Uppercase:", upper_text)
    print("Lowercase:", lower_text)
    print("Word Frequency:", freq)    

    word = input("Enter a word to search: ")
    if word in text.split():
        print(f"'{word}' exists in the text.")
    else:
        print(f"'{word}' not found.")

# Run program
user_text = input("Enter a sentence/paragraph: ")
text_analyzer(user_text)
