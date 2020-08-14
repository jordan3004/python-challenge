import os
import csv
import sys
sys.stdout = open('output/Summary.txt', 'w')
csvpath = os.path.join("Resources", "budget_data.csv")
data = []
months = 0
j = 0
dates = []
total = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #print(row)
        months = months + 1
        diference = int(row[1])-j
        total = total+int(row[1])
        data.append(diference)
        dates.append(row[0])
        j=int(row[1])
        

data.pop(0)
print('Financial Analysis')
print('------------------')
print('Total Months: '+ str(months))
print('Total: ' + "$"+str(total))
#print(data)
maxI = data.index(max(data))+1
maxv = max(data)
minI = data.index(min(data))+1
minv = min(data) 
average = round(sum(data)/(months-1),2)
print("Average  Change: " + "$"+ str(average))
print('Greatest Increase in Profits: '+ dates[maxI] + " ($"+str(maxv)+")")
print('Greatest Decrease in Profits: ' + dates[minI] + " ($"+ str(minv)+")")


sys.stdout.close()

