lst = eval(input())
k = int(input())
l = 0 #skipped indexes at left
max = 0 #length checker , r-l+1 - length
sum = 0

for r in range(len(lst)):
    sum += lst[r]
    if sum <= k and r-l+1 > max:
        max = r-l+1
    while sum > k:
        sum -= lst[l]
        l += 1

print(max)

# [1,2,1,0,1,1,0]