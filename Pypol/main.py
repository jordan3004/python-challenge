import os
import csv
import sys
sys.stdout = open('output/Summary.txt', 'w')
csvpath = os.path.join("Resources", "election_data.csv")
candidates = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #print(row)
        candidates.append(row[2])

    total = len(candidates)
    counter = {}


    for x in candidates:
        if x in counter.keys():
            counter[x] += 1
        else:
            counter[x] = 1

print('Election Results')
print('----------------')
print("Total votes: " + str(total))
print('----------------')
for x in counter:
    perc=counter[x]/total
    percentage = "{:.3%}".format(perc)
    print(x +": " + percentage + "% (" + str(counter[x])+")")

print('----------------')
print("Winner: " + str(max(counter, key=counter.get)))
print('----------------')


sys.stdout.close()

#from collections import Counter
#Names = Counter(candidates).keys() # equals to list(set(words))
#votes = Counter(candidates).values() # counts the elements' frequency
#print(Names)
#print(votes)

