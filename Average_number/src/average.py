#Average
def calculate_average():
    """
    Calculate the average of user-entered numbers.

    The function continuously prompts the user to enter numeric values.
    Input ends when the user presses ENTER without typing a value.

    Behavior:
    - Converts each valid input to float and stores it.
    - Ignores invalid inputs using exception handling.
    - Computes total sum and count of valid numbers.
    - Prints:
        - List of entered numbers
        - Count of numbers
        - A separator line
        - The calculated average
    Edge Cases:
    - If no valid numbers are entered, a message is displayed instead of computing an average.
    """
    numbers:float = []
    total_sum:float = 0

    while True:
        entry:float = input('Enter a Number(ENTER TO STOP):')
    
        if entry == '':
            break
        
        try:
            number = float(entry)
            
            if number < 0 :
                print('Please enter a positive number')
                continue
        except ValueError:
            print('Invalid input')
            continue
    
        numbers.append(number)
        total_sum += number
    
    count:int = len(numbers)

    if count > 0:
        average = total_sum / count
        print('numbers:', numbers)
        print('count:', count)
        print('-' * 50)
        print('average:', average)
        print('-' * 100)
        
    else:
        print('No valid numbers entered')
    
    
    
while True:
    calculate_average()
    
    continue_process= input('\n do you want calculate more?(y(YES)/n(NO))').strip().lower()
    if continue_process in ['y','yes']:
        continue
    elif continue_process  in ['n','no']:
        print ('GoodBye')
        break
    elif continue_process == '':
            break
    else:
        print('Pleae enter a correct respuest.')
        

if __name__ == "__main__":
    calculate_average()