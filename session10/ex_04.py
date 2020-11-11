
#exercise 4
def item_pricing(item):
    c_1 = 0
    c_2 = 1
    length = len(item)

    for i in range(length):
        count = 97 + i
        letter = chr(count) #converted to str
        if item.find(letter,c_1,c_2) == -1:
            print('no')
        else:
            c_1 += 1
            c_2 += 1
            print('yes')
        

        

item_pricing('rice')