def dec_to_hex():
    while True:
        user_entry = input('Enter a decimal number:')
        
        if user_entry == '':
            print('Goodbye')
            break
        
        if not user_entry.isdigit():
            print('invalid input!')
            continue
        
        n = int(user_entry)
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
        
dec_to_hex()  