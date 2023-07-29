str1 = "good morning"

l2 = {}

x = str1.replace(" ","o")

print("replaced ' ' with 'o'")
print(x,"\n")

for i in x:
    l2[i] = l2.get(i,0) + 1

print("Frequency of the elements in the string:",x)
print(l2,"\n")

#l3 = []
s = ""
for i in l2:
    if l2[i] == 1:
        #l3.append(i)
        s = s + str(i)

print("After removing repeated elements")
print(s)
