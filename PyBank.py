
from pathlib import Path
import csv

# Setting the file path
csvpath = Path('budget_data.csv')

# Initializing variables
line_num = 0
month = 0
total = 0
total_old = 0
change = 0
changes = []
dates = []
date = 0


#reading from input file
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
  
    
    for row in csvreader:
        date = row[0]
        month += 1                        #calculates number of months
        total += int(row[1])              #calculates total $$
        change = int(row[1]) - total_old  #calculates monthly changes
        total_old = int(row[1])
        dates.append(date)                #Creates dates list
        changes.append(change)            #Creates monthly changes
        

summary=dict(zip(dates,changes))          #Creates dictionary of months and monthly changes
    
summary.pop('Jan-2010')                   #Takes out the first month


tot_change = 0
count = 0
greatest_icrease = 0
greatest_decrease = 0


for i in summary:
   tot_change += summary[i]              #Calculates total changes over entire period
   count += 1                            #Calculates count of months during which changes occered
    
   if greatest_decrease == 0:
        greatest_decrease = summary[i]
        date_decrease = i
   elif summary[i] > greatest_icrease:  #Determines highest change increase and date
        greatest_icrease = summary[i]
        date_increase = i
   elif summary[i] < greatest_decrease: #Determines lowest change increase and date
        greatest_decrease = summary[i] 
        date_decrease = i
        
print()
print('Financial Analysis')
print()
print('----------------------------------') 
print()
print('Total Months:',month) 
print('Total: $',total)
print('Average Change: $', format(tot_change/count,".2f"))
print('Greatest Increase in Profits:', date_increase, '$(', greatest_icrease, ')')
print('Greatest Decrease in Profits:', date_decrease, '$(', greatest_decrease,')')