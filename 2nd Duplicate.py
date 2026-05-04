lst = eval(input("Enter a list: "))
ele = int(input("Enter a number: "))
c = 3

for i in range(len(lst)):
    if lst[i] == ele:
        c -= 1

    if c == 0:
        print(i)
        break

else:
    print("Does not exist")