#Hex_output
def hex_output():
    dec_value = 0
    hex_string = input('Enter a hex number:')
    
    for power , digit in enumerate(reversed(hex_string)):
        if '0' <= digit <= '9':
            num = int(digit)
        elif 'a' <= digit.lower() <= 'f':
            num = ord(digit.lower()) - 87
        else:
            print('invalid hex digit!')
            return
        
        dec_value +=num*(16**power)
        
    print(dec_value)
    
hex_output()
