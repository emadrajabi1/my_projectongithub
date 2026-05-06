def sum_numbers() -> None:
    """
    Read numbers from user input and compute their sum.
    """
    total: float = 0.0

    while True:
        user_input: str = input('Enter a number: ').strip()
        if not user_input:
            break

        try:
            number: float = float(user_input)
            total += number
            print(f'Current sum: {total}')
        except ValueError:
            print('Invalid number')

    print(f'Final sum: {total}')
    
if __name__ == "__main__":
    sum_numbers()