import math

def mysqrt(a):

    epsilon = 0.0000001
    x = 3

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break 
        x = y
    return x

def test_square_root():
    print('a','\t','mysqrt(a)','\t','math.sqrt(a)','\t','diff')
    print('------------------------------------------------------------')
    for i in range(1,10):
        diff = mysqrt(i) - math.sqrt(i)
        print(i,'\t',f'{mysqrt(i):.11f}','\t',f'{math.sqrt(i):.11f}','\t',diff)

def main():
    test_square_root()

if __name__ == "__main__":
    main()