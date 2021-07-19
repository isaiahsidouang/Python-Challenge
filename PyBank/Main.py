#Import the bank data
import os
import csv

#Define a path to exract data
budget_data_csv = os.path.join('.', 'Desktop', 'Pybank', 'budget_data.csv')

budget_data_csv

#Create lists
total_months = []
total_profit = []
monthly_profit_adjustment = []

with open(budget_data_csv) as csvfile:

# csvreader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Skip header
    csv_header = next(csvreader)
  
    #Iterate through the rows for months
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        
    # Iterate through the profits to find monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_adjustment.append(total_profit[i+1]-total_profit[i])
            
# Get max and min of profit
max_decrease_value = min(monthly_profit_adjustment)
max_increase_value = max(monthly_profit_adjustment)


worst_month = monthly_profit_adjustment.index(min(monthly_profit_adjustment)) + 1
best_month = monthly_profit_adjustment.index(max(monthly_profit_adjustment)) + 1

# Print the code

print("Financial Analysis")
print("-------------------------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_adjustment)/len(monthly_profit_adjustment),2)}")
print(f"Greatest Increase in Profits: {total_months[best_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[worst_month]} (${(str(max_decrease_value))})")

# Print the analysis to the terminal and export a text file with the results
output_data_csv = os.path.join('.', 'Desktop', 'Pybank', 'output_data_csv')

with open(output_data_csv, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_adjustment)/len(monthly_profit_adjustment),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[best_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_value]} (${(str(max_decrease_value))})")
