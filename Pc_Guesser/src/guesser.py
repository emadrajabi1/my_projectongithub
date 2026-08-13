"""
Number Guessing Game (Binary Search)

The computer tries to guess a number that the user has in mind
between 1 and 1000 using binary search.

User inputs:
- 'c' = Correct (computer guessed right)
- 'b' = Bigger (the number is bigger than the guess)
- 's' = Smaller (the number is smaller than the guess)
"""

def main() -> None:
    """Main function to run the number guessing game."""
    
    # Search range
    low: int = 1
    high: int = 1000
    guess: int = 0
    feedback: str = ""
    max_attempts = 8
    attempt = 0
    
    print("Think of a number between 1 and 1000.")
    print("I'll try to guess it!\n")
     

    while feedback != 'c':
        # Binary search: calculate middle point
        guess = (low + high) // 2
        attempt +=1
        
        feedback = input(
            f"Is {guess} your number? (c = correct, b = bigger, s = smaller): "
        ).strip().lower()
        
        if feedback == 'q' or feedback == '' or feedback == '\x1b' :
            print('\n Game exited by user.Goodbye!')
            break

        if feedback == 'b':
            low = guess + 1
        elif feedback == 's':
            high = guess - 1
        elif feedback == 'c':
            print(f"\n🎉 I guessed it! The number is {guess}")
            score = (max_attempts - attempt + 1)*10
            print('Score:',score)
            break
        else:
            print("Invalid input! Please use 'c', 'b', or 's'.")
            
        if attempt >= max_attempts and feedback != 'c':
            print('\n Game Over! You Win , PC is a Loser')
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()