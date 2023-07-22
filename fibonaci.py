num = 56
l = []

if num >= 2:
    l.append(0)
    l.append(1)
    num -= 2

while num:
    n = len(l)
    a = l[n-1]
    b = l[n-2]
    l.append(a + b)
    num -= 1

print("Fibonacci series for the given number is",l)
