year = 2009

if year % 400 == 0:
    print("it is a leap year")
    exit()

if year % 100 == 0:
    print("it is not a leap year")
    exit()

if year % 4 == 0:
    print("it is a leap year")
    exit()

print("it is not a leap year")
