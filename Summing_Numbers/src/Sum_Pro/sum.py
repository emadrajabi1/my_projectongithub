
#Sum_number_P
def sum_advanced():
    total = 0
    count = 0
    largest = None
    smallest = None
    while True:
        user = input('enter number:')
        if user == '':
            break
        try:
            number = int(user)
        except ValueError:
            print('invalid input')
            continue
        total += number
        count +=1
        if largest is  None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
        if count == 0:
            print('No numbers entered')
            return
        average = total / count
        
        print('Total:', total)
        print('Count:', count)
        print('Average:', average)
        print('Largest:', largest)
        print('Smallest:', smallest)
sum_advanced()
