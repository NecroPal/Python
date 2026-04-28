# amt = int(input("Enter withdrawal amount: "))
# bal = 10000
#
# if 1000<amt<=10000:
#     bal = bal - amt
#     print("Amount Withdrawn: ", amt)
#     print("Balance Remaining: ", bal)
# elif amt == bal:
#     print("Minimum balance violation")
# elif amt<=1000:
#     print("Minimum balance violation")
# else:
#     print("Amount exceeding balance")

balance = int(input("Balance: "))
withdrawal = int(input("Withdrawal: "))

if withdrawal > (balance-1000):
    print("Minimum balance Violation")