num1 = 10
num2 = 12

if num2 >= num1:
    b = num2
    a = num1

else:
    b = num1
    a = num2

r = b % a
while r != 0:
    b = a
    a = r
    r = b % a

gcd = a

lcm = int(num1 * num2 / gcd)

print(gcd,lcm)
