s = "string"

l1 = list(s)

l1.reverse()

s1 = ''.join(l1)
print(s1)

i = 0
j = len(s) - 1
s2 = list(s)

while i < j:
    s2[i], s2[j] = s2[j], s2[i]
    i += 1
    j -= 1

s2 = ''.join(s2)
print(s2)
