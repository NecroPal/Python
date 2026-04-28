n=4

for i in range(1, n+1):
    for j in range(1, 2*i):
        print("*", end=" ")
    print()

# for odd numbers
# 2*i+1 - if starting with 0
# 2*i-1 - if starting with 1