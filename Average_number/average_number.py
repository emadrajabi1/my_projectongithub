numbers = []

while True:
    user = input('Enter a number (Enter to stop):')
    
    if user =='':
        break
    
    numbers.append(float(user))
    
average = sum(numbers) / len(numbers)

print('Numbers:', numbers)
print('-' * 30)
print('Average:', average)
