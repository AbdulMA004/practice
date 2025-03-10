arr = [3, 2, 5, 7, 6]
target = 8
dict1 = {}

for index,i in enumerate(arr):
    temp = target - i

    if temp in dict1:
        print(dict1[temp], index)
        break

    dict1[i] = index

a1 = [4, 2, 1, 6]
a2 = [3, 6, 9, 2, 10]
res = []

s = set(a1)

for i in a2:
    if i in s:
        res.append(i)

print(res)
