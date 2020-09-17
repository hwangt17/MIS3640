def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

print(gcd(4,12))
print(gcd(6,12))
print(gcd(9,12))
print(gcd(17,12))