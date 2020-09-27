#exercise 3
team = 'New England Patriots'
new_team = team.upper()
index = team.find('a')
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
# Optional arguments start and end are interpreted as in slice notation. 
# Return -1 if sub is not found.
name = 'bob'

print(new_team)
print(index)
print(team.find('En'))
print(team.find('a', 10))
print(name.find('b', 1, 2)) #letter 'b' not found inbetween 1 and 2.
