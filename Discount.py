amt = int(input("Enter amount: "))
premium = str(input("User is premium(yes/no): "))

if amt >= 5000:
    amt = amt * 0.8
elif amt >= 3000:
    amt = amt * 0.9
else:
    if premium == "yes":
        print("Premium Discount")
    else:
        print("No Discount")

if premium == "yes":
    amt = amt * 0.95

print("Total bill", amt)