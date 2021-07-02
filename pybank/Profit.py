import os
import csv
from decimal import Decimal
import statistics



file = os.path.join('/Users/novakradovic/Git/python-challange/pybank/Resources/budget_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)

    list_of_profit = {'Month': [], 'Profit/Losses': [] }

    for row in ff:
        list_of_profit['Profit/Losses'].append(row[1])

        pro_loss = list_of_profit['Profit/Losses']
    

        type_test = type(pro_loss)

        total_pro = int(sum(Decimal(i) for i in pro_loss))

        avg_change = statistics.mean(Decimal(i) for i in pro_loss)

        max_pro = max(Decimal(i) for i in pro_loss)

       


        
        #total_pro = sum(pro_loss)

    print(max_pro)


