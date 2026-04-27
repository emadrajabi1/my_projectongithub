#Average

numbers = []
total_sum = 0

while True:
    entery = input('Enter a Number(ENTER TO STOP):')
    
    if entery == '':
        break
    
    number = int(entery)
    
    numbers.append(number)
    total_sum +=number
    
count = len(numbers)

if count > 0 :
    average = total_sum / count
    print('numbers:', numbers)
    print('count:', count)
    print('-' * 50)
    print('average:', average)
    
else:
    print('enter number correctly')
    