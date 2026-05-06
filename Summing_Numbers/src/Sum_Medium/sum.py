def sum_numbers() -> None:
    """
    Gets multiple numbers from the user and shows the running sum.
    """
    numbers: list[int] = []
    total: int = 0

    print("Enter numbers one by one.")
    print("Press Enter (empty) to finish.\n")

    while True:
        user_input: str = input('Enter a number: ').strip()

        if user_input == '':
            break

        try:
            number: int = int(user_input)
            numbers.append(number)
            total += number
            print(f'Current sum: {total}')
        except ValueError:
            print('Invalid integer')

    if numbers:
        print('\n' + '=' * 40)
        print(f'Total numbers entered : {len(numbers)}')
        print(f'Final sum : {total}')
        print('=' * 40)
    else:
        print('No numbers were entered.')


if __name__ == "__main__":
    sum_numbers()