import math

#exercise 06
def quadratic(a, b, c):
    """
    please modify it so the function solves the quadratic equation and return two values
    """
    sqrt = math.sqrt((b ** 2) - (4 * a * c))
    x_1 = (-b + sqrt) / (2 * a)
    x_2 = (-b - sqrt) / (2 * a)
    return x_1, x_2

x1, x2 = quadratic(1,5,1)

print('x = ', x1, 'x = ', x2)