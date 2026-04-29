def tray1():
    print("a. Lays 25")
    print("b. Uncle Chips 10")
    print("c. Doritos 30")

    choice = input("Choose a item(a/b/c): ")

    match choice:
        case "a":
            return 25
        case "b":
            return 10
        case "c":
            return 30
        case _:
            print("Invalid choice")
            return 0


def tray2():
    print("a. Coke 25")
    print("b. Pepsi 20")
    print("c. Sprite 30")

    choice = input("Choose a item(a/b/c): ")

    match choice:
        case "a":
            return 25
        case "b":
            return 20
        case "c":
            return 30
        case _:
            print("Invalid choice")
            return 0


def tray3():
    print("a. Dairy Milk 40")
    print("b. KitKat 20")
    print("c. Perk 10")

    choice = input("Choose a item(a/b/c): ")

    match choice:
        case "a":
            return 40
        case "b":
            return 20
        case "c":
            return 10
        case _:
            print("Invalid choice")
            return 0


total = 0

while True:

    print("\n1: Tray1 (Snacks)")
    print("2: Tray2 (Beverages)")
    print("3: Tray3 (Chocolates)")
    print("0: Exit")

    tray = int(input("Select a Tray(1/2/3/0): "))

    if tray == 0:
        break

    match tray:
        case 1:
            while True:
                total += tray1()
                stay = input("Want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        case 2:
            while True:
                total += tray2()
                stay = input("Want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        case 3:
            while True:
                total += tray3()
                stay = input("Want to stay on same tray (y/n): ")
                if stay != "y":
                    break

        case _:
            print("Invalid tray selection")

print("\nTotal :", total, "rupees")
print("Items dispatched ")