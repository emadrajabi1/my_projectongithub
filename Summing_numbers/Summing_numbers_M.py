#Sum_number_M
def Sum_number():
    numbers = []
    while True:
        user = input('Enter a number:')
        
        if user == '':
            break
        
        numbers.append(int(user))
        print(sum(numbers))
    
Sum_number()
