# datetime import sets the current mm/dd/yyyy to be used in birth year calculations
from datetime import date
today = date.today()

# User input and feedback section
print('Welcome to Adam\'s magical, mystical birth year predictor 5000!')
print('What is your name?', end=' ')
user_name = input()
print('Thanks', user_name + '! Now please tell me your age:', end=' ')
user_age = int(input())
print(str(user_age) + '?' ' ' 'Wow, that\'s old!')
print('Last question, can you please enter the number of your birth month? e.g.: Jan = 1, Feb = 2:', end=' ')
birth_month = int(input())

# These formulas are used to calculate the year of birth when using datetime import
birth_year = today.year - user_age
# adjusted_year offsets the birth_year when comparing today.month and birth_month in order to display correct results.
adjusted_year = (today.year - 1) - user_age

# Compares today.month with birth_month in order to calculate the year properly
if birth_month < today.month:
    print('Now with the power of magic, and a bit of science, I know you were born in', str(birth_year) + '!')
else:
    print('Now with the power of magic, and a bit of science, I know you were born in', str(adjusted_year) + '!')

# NameAge program by Adam E. 11/4/2020 IT-140 Module 2-3
