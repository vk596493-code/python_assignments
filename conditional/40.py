password = input("Enter password: ")
if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        if any(ch.isupper() for ch in password):
            print("Valid Password")
        else:
            print("Password must contain uppercase letter")
    else:
        print("Password must contain digit")
else:
    print("Password too short")
