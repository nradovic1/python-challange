import os
import csv
from decimal import Decimal
import statistics
from typing import Counter, ValuesView


file = os.path.join('/Users/novakradovic/Git/python-challange/pybank/Resources/budget_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)
    lines = {'Month': [], 'Profit/Losses': []}
    insert = list(ff)

    for row in insert:
        lines['Profit/Losses'].append(row[1])
    pro_loss = lines['Profit/Losses']
    #pro_loss = (lines['Profit/Losses'])

    

    total_months = len(pro_loss)
    total_pro = (sum(Decimal(i) for i in pro_loss))
    
    for i in pro_loss:
        pro_int = int(i)
        
        if pro_int != (pro_int+1): 
            avg_change = pro_int - (pro_int+1)



        print(avg_change)
        print(pro_int)
    #max_pro = max(Decimal(i) for i in avg_change)
    
    #print(max_pro)

        

    
        
    
        

    

    #list_of_data =  []

    
    #pro_loss = list_of_data.append(ff)
        #list_of_data['Month'].append(row[0:])

    
        #months = list_of_data['Month']
        #int_pro = int(pro_loss)


        #test_list = list(set(pro_loss))
        

        #for i in pro_loss:
        #    change = (i + (i+1))
        
    
        #type_test = type(pro_loss)

        #total_pro = int(sum(Decimal(i) for i in pro_loss))

        #avg_change = round(statistics.mean(Decimal(i) for i in pro_loss),2)

        #max_pro = max(Decimal(i) for i in pro_loss)

        #min_pro = min(Decimal(i) for i in pro_loss)



    print('Financial Analysis')
    print('---------------------------------')
    #print(f'Total Months: {str(total_months)}')
    #print(f'Total: ${str(total_pro)}')
    #print(f'Average Change: ${str(avg_change)}')
    #print(f'Greatest Increase In Profits: ${str(max_pro)}')
    #print(f'Greatest Decrease in Profits: ${str(min_pro)}')