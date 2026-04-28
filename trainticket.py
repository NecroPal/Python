avail = 0
seats = int(input("Seats Required: "))
vip = str(input("Enter VIP status(yes/no): "))

if vip == "yes" or seats <= avail:
    print("Ticket confirmed")
else:
    print("Waiting...")