#arr = [42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
arr = [3,11,4,200]
l = []

for i in arr:
    n = i
    c = 0
    while n != 0:
        c = c + 1
        n = int(n / 10)

    if c % 2 == 0:
        l.append(i)

print(l)
