def password_strength(password):
    length = len(password) >= 8
    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special = any(not ch.isalnum() for ch in password)

    if length and upper and lower and digit and special:
        return "strong password"
    elif length and ((upper and lower and digit and special)):
        return 
    else:
        return "Weak"

# Run program
pwd = input("Enter your password: ")
print("Password Strength:", password_strength(pwd))