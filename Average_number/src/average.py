#Average

numbers = []
total_sum = 0

while True:
    entry = input('Enter a Number(ENTER TO STOP):')
    
    if entry == '':
        break
    
    try:
        number = float(entry)
    except ValueError:
        print('Invalid input')
        continue
    
    numbers.append(number)
    total_sum += number
    
count = len(numbers)

if count > 0:
    average = total_sum / count
    print('numbers:', numbers)
    print('count:', count)
    print('-' * 50)
    print('average:', average)
    
else:
    print('No valid numbers entered')
    