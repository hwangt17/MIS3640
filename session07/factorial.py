#exercise 2-1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter a number: "))

print('the factorial of', n, 'is', factorial(n))