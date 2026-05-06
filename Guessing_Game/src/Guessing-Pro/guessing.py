#Guessing_Number(Profecional)
import random
def guessing_game():
    
    """
    Run an interactive number guessing game with difficulty levels.

    The user selects a difficulty level which determines:
    - The range of the random number (low, high)
    - The maximum number of attempts allowed

    Difficulty Settings:
    - easy   → range: 0–100   | attempts: 7
    - medium → range: 0–500   | attempts: 7
    - hard   → range: 0–1000  | attempts: 10

    Behavior:
    - Prompts user to choose a difficulty level.
    - Generates a random number within the selected range.
    - Repeatedly asks the user to guess the number:
        - Input is read as string and converted to int safely.
        - Invalid inputs (non-integer) are handled via ValueError.
        - Out-of-range guesses are rejected.
        - Attempts are counted only for valid, in-range guesses.

    Game Logic:
    - If guess == answer:
        - Displays success message
        - Calculates score based on remaining attempts:
            score = (max_attempts - attempts + 1) * 10
        - Ends the game loop
    - If guess < answer → informs "Too low"
    - If guess > answer → informs "Too high"

    Termination:
    - Ends when the user guesses correctly
    - Or when maximum attempts are reached (game over)

    Returns:
        None

    Exceptions:
        ValueError:
            Raised when input cannot be converted to integer.
            Handled internally to maintain program flow.
    """
    print('choose dificulty : e/m/h')
    level:str = input('Level: e/m/h ').lower()
    
    if level == 'e':
        low,high = 0,100
        max_attempts = 7
    elif level == 'm':
        low,high = 0,500
        max_attempts = 7
    elif level == 'h':
        low,high = 0,1000
        max_attempts = 10
    else:
        print('invalid level')
        return
    answer:int = random.randint(low,high)
    attemps = 0
    while attemps < max_attempts:
        try:
            guess = int(input(f'Enter your guess({low}-{high}):'))
        except ValueError:
            print('Invalid input')
            continue
        if guess < low or guess > high:
            print('out of range')
            continue
        attemps +=1
        if guess == answer:
            score = (max_attempts - attemps + 1)*10
            print('Correct!')
            print('Attempts:', attemps)
            print('Score:',score)
            break
        elif guess < answer:
            print('Too low')
        else:
            print('Too high')
    else:
        print('Game over , the number was:', answer)
while True:
    guessing_game()
    again:str = input('playing again?(y/n):').lower()
    if again !='y':
        break
    
if __name__ == "__main__":
    guessing_game()