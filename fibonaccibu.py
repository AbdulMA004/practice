n = 5

prev = 1; prev2 = 0

for i in range(n):
    cur = prev + prev2
    prev2 = prev
    prev = cur
    

print(cur)
