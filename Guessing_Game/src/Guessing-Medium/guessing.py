#Guessing_Number
import random 
def guess():
    answer = random.randint(0,30)
    
    while True:
        try:
            guess = int(input('guess the number !'))
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
guess()
