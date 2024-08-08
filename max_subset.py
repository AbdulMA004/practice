l = [2, 1, 8, 3, 7, 2, 3, 9]

k = 4

if k > len(l):
    print("insufficient array")

max_sum = sum(l[:k])
#print(max_sum)

i = 0
curr_sum = max_sum
while k<len(l):
    curr_sum += - l[i] + l[k]
    i += 1
    k += 1
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
