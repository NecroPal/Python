n = int(input("Enter last range: "))
sum = 0
for i in range(2, n+1):
    for j in range(2, (i//2)+1):
        if i%j == 0:
            break
    else:
            sum = sum + i
            print(i)
print("sum: ", sum)