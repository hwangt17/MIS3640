def sum_all():
    """
    calculates the sum of integers from 1 to 1000, and prints the sum
    """
    current_sum = 0

    for i in range(1,1001):
        print(f'Iteration {i}:')
        print(f'The value of i is {i}')
        current_sum = current_sum + i
        print(f'Currently, the sum is {current_sum}.')
        print()

    print(current_sum)

def sum_odd():
    """
    calculates the sum of odd mumbers from 1 to 1000, and prints the sum
    """
    current_sum = 0

    # for i in range(1,1001):
    #     print(f'Iteration {i}:')
        
    #     if i % 2 == 1:
    #         print(f'The value of i is {i}')
    #         current_sum = current_sum + i
    #         print(f'Currently, the sum is {current_sum}.')
            
    #     print()

    for i in range(1,1001,2):
        print(f'The value of i is {i}')
        current_sum = current_sum + i
        print(f'Currently, the sum is {current_sum}.')
        print()
        
    print(f'The final result is {current_sum}.')

def countdown(n):
    import time
    while n > 0:
        print(n)
        n = n - 1
        time.sleep(1)
    print('Blastoff!')

def break_demo():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print('Done!')

def main():
    sum_all()
    #sum_odd()
    #countdown(5)
    #break_demo()

if __name__ == "__main__":
    main()