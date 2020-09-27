#exercise 5
def any_lowercase1(s):
    """
    If the string in variable s has all lowercase in it, return True. If not, return False.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    """
    If the string in variable 'c' is lowercase, return True. If not, return False.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """
    Store whether string in variable s has any lowercase in it in flag and return the flag. 
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """
    If the string in variable s has any lowercase in it, return True. If not, return False.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """
    If the string in variable s does not all have lowercase in it, return False. If not, return True.
    """
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase1('Back'))
print(any_lowercase2('BACK'))
print(any_lowercase3('BACK'))
print(any_lowercase4('BACK'))
print(any_lowercase5('Back'))