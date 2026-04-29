#Guessing_Number_M
import random
def guess():
    answer = random.randint(0,500)
    
    while True:
        try:
            guess = int(input('tell me your guess:'))
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
         
guess()