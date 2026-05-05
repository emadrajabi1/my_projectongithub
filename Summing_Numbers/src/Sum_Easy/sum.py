#Sum_number
def Sum_number():
    total = 0
    while True:
        user = input('Enter a number:')
        
        if user == '':
            break
        
        total += int(user)
        print(total)
    
Sum_number()
