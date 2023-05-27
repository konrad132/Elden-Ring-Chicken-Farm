import time
import datetime
from Shortcuts import countdowntimer, mainloop, calculated_runes_earned, time_estimate

# Arrow Warning
print(' !!! Make sure you have enough arrows in your inventory to complete all of the loops !!!')

# Enter how many loops you want to do
loops = int(input('How many loops do you want to do?'))
time_estimate(loops)

# Rune Calculator
while True:
    run_calc = input('Do you want to run rune Calculator?')
    if run_calc.lower() == 'yes' or run_calc.lower == 'y':
        current_runes = int(input('How many runes do you currently have?'))
        chicken_value = int(input('How many runes is the chicken worth?'))
        calculated_runes_earned(chicken_value, loops, current_runes)
    elif run_calc.lower() == 'no' or run_calc.lower() == 'n':
        break
    else:
        run_calc = input('Invalid answer please write Yes or No')

# Run Program
while True:
    decision = input(' Do you want to run the farm for {} loops ?'.format(loops))
    if decision.lower() == 'yes' or decision.lower() == 'y':
        # Start Farming.
        countdowntimer(0, 3)  # Countdown timer
        start_time = time.time()
        mainloop(loops)
        total_time = str(datetime.timedelta(seconds=(time.time() - start_time)))
        total_time_split = total_time.split(':')
        print('Total Time was', total_time_split[0], ' Hours', total_time_split[1], ' Minutes', total_time_split[2],
              ' Seconds')

    elif decision.lower() == 'no' or decision.lower() == 'n':
        print('Program has been terminated')
        exit()
    else:
        decision = input('Invalid answer please write Yes or No')
