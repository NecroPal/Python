lst = eval(input("Enter a list: "))
n = int(input("Enter n: "))

temp = lst.copy()

for _ in range(n):
    min = temp[0]
    for i in temp:
        if i < min:
            min = i
    temp.remove(min)

nth_smallest = min

temp = lst.copy()

for _ in range(n):
    max = temp[0]
    for i in temp:
        if i > max:
            max = i
    temp.remove(max)

nth_largest = max


print(nth_largest, nth_smallest)