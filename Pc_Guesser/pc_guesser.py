import random
a = 1
z = 1000
pc = ''

while pc != 'c':
    guess = (a+z)//2
    pc = input(f'is this the number: {guess}? (c,b,s)')
    if pc == 'b':
        a = guess +1
    elif pc == 's':
        z = guess-1
        
print(guess)
