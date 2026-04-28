password = input("Enter a password: ")
hasUpper = False
hasDigit = False
hasSymbol = False
hasLen = len(password) >= 8

for i in password:
    if i.isupper():
        hasUpper = True
    elif i.isdigit():
        hasDigit = True
    elif i.islower():
        hasLower = True
    else:
        hasSymbol = True

if hasUpper and hasDigit and hasSymbol and hasLen:
    print("Password is Strong")
else:
    print("Password is Weak")