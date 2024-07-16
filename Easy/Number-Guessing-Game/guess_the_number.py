import random
import logo_art

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty_level(level):
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return None

def check_answer(guessed_number, answer):
    if guessed_number < answer:
        if answer - guessed_number <= 3:
            print('Your guess is too low, but very close.')
        else:
            print('Your guess is too low.')
        return False
    elif guessed_number > answer:
        if guessed_number - answer <= 3:
            print('Your guess is too high, but very close.')
        else:
            print('Your guess is too high.')
        return False
    else:
        print(f'Your guess is right...The answer was {answer}')
        return True

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 50")
    answer = random.randint(1, 50)
    # print(answer)  # Remove this line for the final version
    level = input("Choose level of difficulty...Type 'easy' or 'hard': ")
    attempts = set_difficulty_level(level)
    
    if attempts is None:
        print("You have entered wrong difficulty level... PLAY AGAIN!!")
        return
    
    guessed_number = 0
    while attempts > 0:
        print(f'You have {attempts} remaining guesses to guess the number')
        try:
            guessed_number = int(input("Guess a number: "))
            if guessed_number < 1 or guessed_number > 50:
                print("Please enter a number between 1 and 50.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if check_answer(guessed_number, answer):
            return
        
        attempts -= 1
        
        if attempts == 0:
            print("You are out of guesses... You LOSE!")
            return
        else:
            print('Guess Again')

def play_again():
    while True:
        replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if replay == 'yes':
            game()
        elif replay == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

game()
play_again()
