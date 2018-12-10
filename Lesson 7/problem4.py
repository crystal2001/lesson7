print('-' * 80)

print('Morbid Predictions Program:')

print()

print('Description: This program askes you for your current age and tells you the year that you will die (on average)')

age = input ('What is your age today? ')
age = int(age)

result = 100 - age

year = age + 2018

print('You will die in the year...' + str(year) + '.')