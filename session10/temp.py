def calc(x):
    result = 0
    for i in range(x+1):
        print(i, result)
        result += i
    return result

def main():
    y = 10
    my_result = calc(5)
    print(my_result())

if __name__ == "__main__":
    main()