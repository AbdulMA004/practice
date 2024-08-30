def sub(i,l,sum1,a):
    if i == len(a):
        if sum1 == fs:
            l1.append(l.copy())
            
        return

    l.append(a[i])
    sum1 += a[i]
    sub(i+1,l,sum1,a)
    l.pop()
    sum1 -= a[i]
    sub(i+1,l,sum1,a)

a = [1,2,1]
fs = 3
l = []
l1 = []
sum1 = 0
sub(0,l,sum1,a)
print(l1)
