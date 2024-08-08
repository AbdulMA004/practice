l = [1, 5, 3, 6, 2, 1, 3, 9, 0]

if len(l) < 1:
    print("array insufficient")

i = 0
j = 0
res = []
l1 = []

while j < len(l):
    if l[j] not in l1:
        l1.append(l[j])
        #print(l1)
        j += 1

    else:
        i += 1
        if len(res) < len(l1):
            #print(l1, res)
            res = l1.copy()
        j = i
        l1 = []

if len(res) < len(l1):
    res = l1.copy()

print(res)
