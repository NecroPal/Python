flag = 0

for i in range(3):
    password = input("Enter your password: ")

    if password == "352":
        print("Login successful")
        flag = 1
        break
    else:
        print("Wrong attempt")

if not flag:
    print("Account Locked")