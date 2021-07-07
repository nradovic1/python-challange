import os
import csv
from decimal import Decimal
import statistics
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
    
        #type_test = type(pro_loss)

    total_pro = int(sum(Decimal(i) for i in pro_loss))

    

    avg_change = round(statistics.mean(Decimal(i) for i in pro_loss),2)

    max_pro = max(Decimal(i) for i in pro_loss)

    min_pro = min(Decimal(i) for i in pro_loss)

original_stdout = sys.stdout
with open("output_pybank.txt", "w") as ft:

    sys.stdout = ft
    print('Financial Analysis')
    print('---------------------------------')
    print(f'Total Months: {str(total_months)}')
    print(f'Total: ${str(total_pro)}')
    print(f'Average Change: ${str(avg_change)}')
    print(f'Greatest Increase In Profits: ${str(max_pro)}')
    print(f'Greatest Decrease in Profits: ${str(min_pro)}')
    sys.stdout = original_stdout
    
  


