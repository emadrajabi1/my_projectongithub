import statistics

def run_timing_advanced() -> None:
    
    """
    Read KM inputs and print count, mean, min, and max.
    Stops on empty input. Ignores invalid and negative values.
    """
    
    runs = []
    while True:
        user_input:str = input('Enter how many KM for this Run: ').strip()
        if not user_input:
            break
        
        try:
            run_time:float = float(user_input)
            if run_time < 0 :
                print ('DO NOT ENTER NEGATIVE TIME.')
                continue
            runs.append(run_time)
        except ValueError:
            print('ENTER NUMBER PLEASE.')
            continue
    if runs:
        average = statistics.mean(runs)
        shortest = min(runs)
        longest = max(runs)
        
        print('-' * 30)
        print(f'How many time : {len(runs)}')
        print(f'Shortest:{shortest:.2f}')
        print(f'Longest:{longest:.2f}')
        print('-' * 30)
        print('No data to calculate.')
        
if __name__ == "__main__":
    run_timing_advanced()
