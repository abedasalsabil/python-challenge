
import csv
import os


filename = '../PyBank/Resources/budget_data.csv'


def budget_csv(filename, output_filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        data = list(csv_reader)

    # Calculate total number of months
    total_months = len(data)

    # Calculate net total amount of "Profit/Losses"
    net_total = sum(int(row[1]) for row in data)

    # Calculate changes in "Profit/Losses" and average of changes
    changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(len(data)-1)]
    average_change = sum(changes) / len(changes)

    # Find the greatest increase in profits
    max_increase = max(changes)
    max_increase_date = data[changes.index(max_increase)+1][0]
    # Find the greatest decrease in profits
    max_decrease = min(changes)
    max_decrease_date = data[changes.index(max_decrease)+1][0]

    results = "Financial Analysis\n"
    results += "------------------\n"
    results += f"Total Months: {total_months}\n"
    results += f"Net Total: ${net_total}\n"
    results += f"Average Change: ${average_change:.2f}\n"
    results += f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    results += f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n"

    with open(output_filename, 'w') as output_file:
        output_file.write(results)

    print(results)


output_filename = 'analysis/results.txt'
budget_csv(filename, output_filename)
