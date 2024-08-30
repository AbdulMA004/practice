#l1 = []
def sub(i,l,a):
    if i == len(a):
        l1.append(l.copy())
        return
    l.append(a[i])
    sub(i+1,l,a)
    l.pop()
    sub(i+1,l,a)

a = [3,2,1]
l=[]
l1=[]
sub(0,l,a)
print(l1)
