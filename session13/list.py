# list is sequence
# [10, 20, 30, 40]
# ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# ['spam', 2.0, 5, [10, 20]]

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

#lists are mutable
# AFC_east[3] = 'New York Giants'
# print(AFC_east)

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print('Buffalo Bills' in AFC_east)

# Exercise 1
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]
apple_index = L[0].index('Apple')
print(apple_index)
lisa_index = L[2].index('Lisa')
print(lisa_index)
rail_index = L[1][2].index('On Rail')
print(rail_index)

# traversing a list
# for team in AFC_east:
#     print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants'], [1, 2, 3]]
print(len(my_list))

# list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# list slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)