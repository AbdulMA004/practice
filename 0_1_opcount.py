l = [0, 1, 0, 1, 1, 1, 0, 1, 0]

s = sum(l)
count = len(l) - s
i = 0;j = 0
shift = 0

while i < len(l) and count != 0:
    if l[i] == 0:
        count -= 1

        if j != 0:
            l[i-j], l[i] = l[i], l[i-j]
            shift += j
            

    else:
        j += 1
    i += 1
print(l,shift)
