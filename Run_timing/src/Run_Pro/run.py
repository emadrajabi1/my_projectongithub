import statistics

def run_timing_advanced():
    runs = []
    while True:
        user_input = input('Enter how many time KM do you Run: ').strip()
        if not user_input:
            break
        
        try:
            run_time = float(user_input)
            if run_time < 0 :
                print ('DO NOT ENTER NEGATIVE TIME.')
            
                continue
            runs.append(run_time)
        except ValueError:
            print('ENTER NUMBER PLEASE.')
            continue
    if runs:
        average = statistics.mean(runs)
        fatest = min(runs)
        slowest = max(runs)
        
        print('-' * 30)
        print(f'How many time : {len(runs)}')
        print(f'Fatest:{fatest:.2f}')
        print(f'Slowest:{slowest:.2f}')
        print('-' * 30)
        print('there is not anything for calculating.')
        
run_timing_advanced()