#Hex_output
def hex_output():
    while True:
        hex_string = input('Enter a hex number:')
    
        if hex_string == '':
            print('Goodbye!')
            break
        
        print(f'Your input: {hex_string}')
    
        dec_value = 0    
        valid_input = True
    
        for power , digit in enumerate(reversed(hex_string)):
            if '0' <= digit <= '9':
                num = int(digit)
            elif 'a' <= digit.lower() <= 'f':
                num = ord(digit.lower()) - 87
            else:
                print('invalid hex digit!')
                valid_input = False
                break
            dec_value +=num*(16**power)
        
        if valid_input:
            print(f'Decimal value: {dec_value}')
        
            print('-' * 30)
    
    
if __name__ == "__main__":
    hex_output()

