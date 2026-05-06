def dec_to_hex():
    """
    Convert decimal numbers (base 10) to hexadecimal (base 16).

    The function runs in a loop, allowing multiple conversions until the user exits.

    Behavior:
    - Prompts the user to enter a decimal number as a string.
    - If the input is empty → terminates the program with a goodbye message.
    - Validates input using `str.isdigit()` to ensure only non-negative integers.
    - Converts valid input to integer.
    - Handles the special case where the number is 0.
    - Converts the number to hexadecimal manually using division by 16:
        - Repeatedly divides the number by 16.
        - Stores remainders.
        - Maps remainders to hexadecimal characters (0–9, A–F).
        - Reverses the result to obtain the correct order.

    Output:
    - Displays the original decimal input.
    - Displays the corresponding hexadecimal value.
    - Prints a separator line after each conversion.

    Loop:
    - Continues until the user enters an empty string.

    Returns:
        None

    Limitations:
    - Does not handle negative numbers or non-integer values.
    """
    while True:
        user_entry:int = input('Enter a decimal number:')
        
        if user_entry == '':
            print('Goodbye')
            break
        
        if not user_entry.isdigit():
            print('invalid input!')
            continue
        
        n:int = int(user_entry)
        print(f' your input:{n}')
        
        if n == 0:
            print('Hex_value:0')
            print('-'*30)
            continue
        
        hex_digits = '0123456789ABCDEF'
        result = ''
        
        while n > 0:
            reminder = n %16
            result +=hex_digits[reminder]
            n //= 16
            
        result = result[::-1]
        
        print(f'Hex_value:{result}')
        print('-'*50)
        
if __name__ == "__main__":
    dec_to_hex()
          