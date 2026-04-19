#Guessing_Number(Profecional)
import random
def guessing_game():
    print('choose dificulty : easy/medium/hard')
    level = input('Level: ').lower()
    
    if level == 'easy':
        low,high = 0,50
        max_attempts = 7
    elif level == 'medium':
        low,high = 0,100
        max_attempts = 7
    elif level == 'hard':
        low,high = 0,500
        max_attempts = 10
    else:
        print('invalid level')
        return
    answer = random.randint(low,high)
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
    again = input('playing again?(yes/no):').lower()
    if again !='yes':
        break
    