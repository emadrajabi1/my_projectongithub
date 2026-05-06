#Guessing_Number_M
import random
def guess():
    
    """
    Run a number guessing game.

    The program generates a random integer between 0 and 500.
    The user repeatedly attempts to guess the number.

    Behavior:
    - Prompts the user to input an integer.
    - Handles invalid (non-integer) inputs using exception handling.
    - Compares the guess with the generated number:
        - If equal → prints 'correct' and exits loop.
        - If greater → informs the user the answer is smaller.
        - If smaller → informs the user the answer is larger.

    Loop:
    - Continues indefinitely until the correct number is guessed.

    Returns:
        None
    """
    answer:int = random.randint(0,500)
    
    while True:
        try:
            guess:int = int(input('tell me your guess:'))
        except ValueError:
            print('wrong number have been entered')
            continue
        if guess >= 500 or guess <= 0 :
            print('number out of range')
            continue
        if guess == answer:
            print('youre Hit the number, Correct!')
            break
        elif guess < answer:
            print('Help:number is Bigger')
        else:
            print('Help:number is Lower')
         
if __name__ == "__main__":
    guess()