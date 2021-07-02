import os
import csv


file = os.path.join('/Users/novakradovic/Git/python-challange/pypoll/Resources/election_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)

    data = {'Voter': [], 'ID County': [], 'Candidate': []}

    for row in ff:
        
        
        data['Candidate'].append(row[2])

        
        Candidate = (data['Candidate'])

    total_votes = len(Candidate)

    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for vote in Candidate:
        if vote== 'Khan':
            khan = khan + 1
        elif vote == 'Correy':
            correy = correy + 1
        elif vote == 'Li':
            li = li + 1
        else: 
            otooley = otooley + 1

    khan_f = float(khan)
    khan_per = format(((khan/total_votes)*100), '.4f')
    correy_f = float(correy)
    correy_per = format(((correy/total_votes)*100), '.3f')
    li_f = float(li)
    li_per = format(((li/total_votes)*100), '.3f')
    otooley_f = float(otooley)
    otooley_per = format(((otooley/total_votes)*100), '.3f')

    list_of_votes = [(khan), (correy), (li), (otooley)]
    winner = max(list_of_votes)

    print('Election Results')
    print('------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('------------------------------------')
    print(f'Khan: {khan_per}% ({khan})')
    print(f'Correy: {correy_per}% ({correy})')
    print(f'Li: {li_per}% ({li})')
    print(f"O'Tooley: {otooley_per}% ({otooley})")
    print('------------------------------------')

    if winner == (khan):
        print('Wiiner: Khan')
    elif winner == (correy):
        print('Winner: Correy')
    elif winner == (li):
        print('Winner: Li')
    else:
        print("Winner: O'Tooley")
    
    print('------------------------------------')



    
    

    
    #print(f'Khan: {khan_per}% ({khan})')
    #print(f'Correy: {correy_per}% ({correy})')
    #print(f'Li: {li_per}% ({li})')
    #print(f"O'Tooley: {otooley_per}% ({otooley})")

    