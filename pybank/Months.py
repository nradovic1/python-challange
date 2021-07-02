import os
import csv

file = os.path.join('/Users/novakradovic/Git/python-challange/pybank/Resources/budget_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)

    list_of_months = []

    for row in ff:
        list_of_months.append(row)
        month = list_of_months[0:]
        total_months = len(month)

    print(f'Total Months: {str(total_months)}')

    def month_outcome(data):
        month = list(str(data[0]))
        total_months = len(month)
        
        print(f'Total Months: {str(total_months)}')

   

    for row in ff:
        month_outcome(row)


    




       



