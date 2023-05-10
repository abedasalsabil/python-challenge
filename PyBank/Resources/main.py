import os
import csv

PyBankcsv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')


with open(PyBankcsv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    data = list(csv_reader)

# Calculate total number of months
total_months = len(data)

# Calculate net total amount of "Profit/Losses"
net_total = sum(int(row[1]) for row in data)

# Calculate changes in "Profit/Losses" and average of those changes
changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(len(data)-1)]
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_increase_date = data[changes.index(max_increase)+1][0]
max_decrease = min(changes)
max_decrease_date = data[changes.index(max_decrease)+1][0]

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

text_file = ('..', 'analysis', 'PyBank_text_file.txt')

with open(text_file, "w") as textfile:
    textfile.write("Financial Analysis" + "\n")
    textfile.write("------------------------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Net Total Total: $ {net_total}\n")
    textfile.write(f"Average Change: $ {average_change:.2f}\n")
    textfile.write(
        f"Greatest Increase in Profits: $ {max_increase_date}, ($ {max_increase})\n")
    textfile.write(
        f"Greatest Decrease in Profits: $ {max_decrease_date}, ($ {max_decrease})\n")
