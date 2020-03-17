# Angeline Hidalgo
# February 2, 2020

# Defines set variables for different days of the week from 0 - 6.
# 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday
def which_day(start, nights):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    return days[(start + nights) % 7]  # Equation for calculating the return day.

# Prompts the user to enter what day they are leaving. In this case, you will leave on Wednesday (3).
start_day = int(input('Assuming that 0 is Sunday and 6 is Saturday, what day are you leaving: '))
# Prompts the user to enter how many days they will be gone.
end_day = int(input('How many days will you be gone: '))

# Prints out the day they will return.
print('You will return on: ')
print(which_day(start_day, end_day))  # Saturday
