l1 = [1,2,3,1,2,7,9,4,5,3,5]

l2 = {}

j = 0
for i in l1:
    l2[i] = l2.get(i,0) + 1

print(l2)

l3 = []
for i in l2:
    if l2[i] == 1:
        print(i,end=" ")
        l3.append(i)

print(end="\n")
print(l3)
