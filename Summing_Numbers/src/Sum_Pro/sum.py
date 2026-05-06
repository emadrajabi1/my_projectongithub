
#Sum_number_P
def sum_advanced():
    """
Read numeric inputs and compute summary statistics.

.. behavior::
   - Empty input terminates execution
   - Non-numeric input is ignored
   - Tracks min/max incrementally
"""
    total:float = 0
    count:int = 0
    largest:float = None
    smallest:float = None
    while True:
        user = input('enter number:')
        if user == '':
            break
        try:
            number:float = int(user)
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
        
if __name__ == "__main__":
    sum_advanced()
