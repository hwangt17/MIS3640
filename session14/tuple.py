# a = 10
# b = 90
# temp = a
# a = b
# b = temp
# print(a, b)

# a, b = b, a

# email = 'zli@babson.edu'
# id, domain = email.split('@')
# print(id)
# print(domain)

# t = divmod(7, 3)
# print(t)

# def printall(*args): # A parameter name that begins with * gathers arguments into a tuple.
#     print(args)
    
# printall(1, 2.0, '3')
# printall(1, 2.0, '3', None, True)


# t = (7, 3)
# divmod(*t)


# exercise01
def sumall(*args):
    return sum(args)

print(sumall(1,2,3,4,5))


# s = 'abc'
# t = [0, 1, 2]
# print(zip(s, t))

# for pair in zip(s, t):
#     print(pair)

# print(list(zip(s, t)))

# def has_match(t1, t2):
#     for x, y in zip(t1, t2):
#         if x == y:
#             return True
#     return False

# print(has_match('age','ege'))

# for index, element in enumerate('abc'):
#     print(index, element)

# d = {'a':0, 'b':1, 'c':2}
# t = d.items()
# print(t)

# for key, value in d.items():
#     print(key, value)


# exercise02-1
def most_frequent(s):
    """
    function takes in a string and prints the letters in decreasing order of frequency.
    """
    d = dict()
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print(most_frequent('google'))
