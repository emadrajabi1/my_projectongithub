def run_timing():
    """ Calculates the running average of kilometers run by the user.
    
This function continuously prompts the user to enter the kilometers they have run.
After each valid input, it calculates and displays the average distance so far.
The program exits when the user presses Enter without entering any value.
Handles invalid inputs gracefully with an error message. """

    number_of_runs:int = 0
    total_km:float = 0
    
    while True:
        one_run:str = input('Enter how many KM do you Run: ')
        if not one_run:
            break
        try:
            km = float(one_run)
        except ValueError:
            print('Invalid input')
            continue
        number_of_runs += 1
        total_km += km
        average_km = total_km / number_of_runs
        print(f'Average of {average_km:.2f} km over {number_of_runs} runs')
 
if __name__ == "__main__":
    run_timing()
