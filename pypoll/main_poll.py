import os
import csv


file = os.path.join('/Users/novakradovic/Git/python-challange/pypoll/Resources/election_data.csv')

with open(file, 'r') as csvfile:
    ff = csv.reader(csvfile, delimiter=',')

    next(ff)

    data = {'Voter': [], 'ID County': [], 'Candidate': []}

    for row in ff:
        data['Voter'].append(row[0])
        data['ID County'].append(row[1])
        data['Candidate'].append(row[2])

        voter = list(data['Voter'])
        ID_County = list(data['ID County'])
        Candidate = (data['Candidate'])

    total_votes = len(Candidate)
    set_voter = set(data['Candidate'])
    
    print('hello')
    