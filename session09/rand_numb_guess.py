import random


# 1. Assign random number between 1 - 20 and store in rand_num
# 2. Prompt user to input(string) name and store in user_name 
# 3. Start a for loop i in range of 5
# 4. Prompt user to input a number(int) between 1- 20 and store it in user_guess.
# 5. If user_guess is greater than rand_num then return “your guess is too high”
# 6. Else if user_guess is less than rand_num then return “your guess is too low”
# 7. Else user_guess equals rand_num then return “Good job {user_name}! You guessed my number in {i+1} times” then break
# 8. After 6 tries, Return “You lose!”


def guess_game(max_num = 20, total_tries = 6):
    """
    This is a random number guessing game. 
    Guess a number between 1 - 20 with total 6 tries to guess the number correct. 
    The program will tell us if the guess is too high or too low.
    The maximum random number is max_num, 20 (default).
    The total number of tries is total_tries, 6 (default).
    """


    rand_num = random.randrange(1,max_num+1)

    user_name = str(input('Hello! What is your name? '))
    print(f'Well, {user_name}, I am thinking of a number between 1 and {max_num}.')

    for i in range(total_tries):
        user_num = int(input('Take a guess: '))
        if user_num > rand_num:
            print('your guess is too high')
        elif user_num < rand_num:
            print('your guess is too low')
        elif user_num == rand_num:
            print(f'Good job {user_name}! You guessed my number in {i+1} times')
            break
    if user_num != rand_num:
        print(f'Nope, the number I was thinking of is {rand_num}')


def main():
    guess_game()

if __name__ == "__main__":
    main()