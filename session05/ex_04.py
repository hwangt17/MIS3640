#exercise 04
def my_abs(x):
    return abs(x)

neg_nub = -14.2

#exercise 05
result_int = isinstance(neg_nub,int)
result_flo = isinstance(neg_nub,float)
if result_int == True or result_flo == True:
    print(my_abs(neg_nub))
else:
    print('not integers or floating numbers')
