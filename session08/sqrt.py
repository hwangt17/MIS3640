# a = 4
# x = 3
# y = (x + a/x) / 2
# print(y)


# x = y
# y = (x + a/x) / 2
# print(y)


a = 4
x = 3
epsilon = 0.00000001

while True:
    y = (x + a/x) / 2
    if abs(y-x) < epsilon:
        break
    x = y
print(x)