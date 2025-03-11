arr = [3, 2, 5, 7, 6]
target = 8
dict1 = {}

for index,i in enumerate(arr):
    temp = target - i

    if temp in dict1:
        print(dict1[temp], index)
        break

    dict1[i] = index

