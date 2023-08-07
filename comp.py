s1 = "23"
s2 = "1"
eq = 1

#Method1
if len(s1) == 0 and len(s2) != 0 or len(s1) != 0 and len(s2) == 0:
    print("Both are not equal and not same")
    exit()

for i in range(0,len(s1)):
    if s1[i] != s2[i]:
        eq = 0
        break
if eq == 1 and len(s1) == len(s2):
    print("Both are equal and same")

elif eq == 0 and len(s1) == len(s2):
    print("Both are equal but not same")

else:
    print("Both are not equal and not same")

#Method2
if s1 == s2:
    print("Both are equal and same")

elif len(s1) == len(s2):
    print("Both are equal but not same")

else:
    print("Both are not equal and not same")
