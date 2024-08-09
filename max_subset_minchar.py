l = ['a', 'b', 'c', 'f', 'e', 'f', 'x']

k=2; i = 0; j = 0
dict1 = {}
l1 = []
res = []
while i < len(l) and j < len(l):
        if l[j] not in dict1 and len(dict1) < 3:
            dict1[l[j]] = 0
            l1.append(l[j])
            j += 1
            #print(len(dict1))

        elif l[j] in dict1:
            dict1[l[j]] += 1
            l1.append(l[j])
            j += 1

        else:
            i += 1
            j = i
            if len(res) < len(l1):
                res = l1.copy()
            l1 = []
            dict1 = {}

if len(res) < len(l1):
    res = l1.copy()

print(res)

         




