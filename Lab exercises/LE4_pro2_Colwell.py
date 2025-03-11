# Written by Jayden Colwell
def power(n, exp):
    if exp == 0:
        return 1
    else:
        return n * power(n, exp - 1)

n = 3
exp = 4
print(power(n, exp))