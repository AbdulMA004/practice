year = 2007
l2 = []

l1 = list(str(year))
l1[2:4] = [''.join(l1[2:4])]
a = l1.pop()


print("Extracted last two number of the given year:",a)

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

print("Current time",current_time)


time1 = "09:12:00pm"
lt = list(time1)

if lt[0] == '1' and lt[1] == '2':
    if lt[8] == 'a':
        lt[0] == '0'
        lt[1] == '0'

elif lt[8] == 'p':
    lt[0] = int((int(lt[1]) + 12) / 10)
    lt[1] = int((int(lt[1]) + 12) % 10)

lt.pop()
lt.pop()
g = map(str, lt)
g1 = ''.join(g)
print("Time changes to 24 hour format",g1)
