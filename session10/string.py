team = 'New England Patriots'
letter = team[1]
print(letter)

print(team[0])

print(len(team))

last = team[len(team)-1]
print(last)

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index = index + 1

for letter in team:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))
