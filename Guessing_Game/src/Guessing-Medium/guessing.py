#Guessing_Number
import random 
def guess():
    
    """
    Run a number guessing game.

    A random integer is generated between 0 and 500.
    The user repeatedly inputs guesses until the correct number is found.

    Behavior:
    - Reads input as string, then converts to integer in a controlled block.
    - Handles invalid (non-integer) input using ValueError.
    - Compares the guess with the target number:
        - Equal  → prints 'correct' and exits loop.
        - Greater → informs the user the answer is smaller.
        - Smaller → informs the user the answer is larger.

    Loop:
    - Continues indefinitely until the correct guess is entered.

    Returns:
        None

    Exceptions:
        ValueError:
            Raised internally when input cannot be converted to int.
            Handled to prevent program termination.
    """
    answer = random.randint(0,500)
    
    while True:
        try:
            guess:int = int(input('guess the number : '))
        except ValueError:
            print('is not correct.')
            continue
        if guess == answer:
            print('correct')
            break
        elif guess > answer:
            print('answer is less than your guess')
        else:
            print('answer is more than your guess')
            
if __name__ == "__main__":
    guess()
