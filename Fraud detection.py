amt = int(input("Enter amount: "))
location = str(input("Location Match(yes/no): "))
transactions = 0

for i in range(3):
    if amt > 50000 and location == "yes":
        print("Fraud Detected")
    elif transactions > 3:
