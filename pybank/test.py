import os
import csv
import sys


file = os.path.join('/Users/novakradovic/Git/python-challange/pybank/Resources/budget_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)

    list_of_data = {'Month': [], 'Profit/Losses': [] }

    for row in ff:
        list_of_data['Profit/Losses'].append(row[1])
        list_of_data['Month'].append(row[0])

        pro_loss = list_of_data['Profit/Losses']
        months = list_of_data['Month']

        total_months = len(months)


original_stdout = sys.stdout
with open("analysis", "filetest.txt", "w") as ft:

    sys.stdout = ft
    print('Financial Analysis', file=ft)
    print('---------------------------------')
    print(f'Total Months: {str(total_months)}')
    sys.stdout = original_stdout

