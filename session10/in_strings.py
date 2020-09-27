#exercise 2
def count(word,letter):
    """
    Count selected letter in a given word. 
    """
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

#exercise 3
team = 'New England Patriots'
new_team = team.upper()
index = team.find('a')
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
# Optional arguments start and end are interpreted as in slice notation. 
# Return -1 if sub is not found.
name = 'bob'

#exercise 4
def item_pricing(item):
    c_1 = 0
    c_2 = 1
    length = len(item)

    for i in range(length):
        count = 97 + i
        letter = chr(count) #converted to str
        if item.find(letter,c_1,c_2) >= 0:
            print("ok")
        else:
            count = count + 1
            print("nope")

          
def main(): 
    #count('Facebook','')

    # print(new_team)
    # print(index)
    # print(team.find('En'))
    # print(team.find('a', 10))
    # print(name.find('b', 1, 2)) #letter 'b' not found inbetween 1 and 2.

    item_pricing('baba')

if __name__ == "__main__":
    main()