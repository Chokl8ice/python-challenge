import os
import csv

budget_data_csv = os.path.join('..', '02-Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
budget_data_csv = "../Resources/budget_data.csv"

total_months = 0
total_profit = 0
monthly_change = 0
previous_monthly_change = 0

increase = ["", 0]
decrease = ["", 10**9]

With open(budget_data_csv) as Revenue Data
    reader = csv.DictReader(Revenue_Data)
    For row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        monthly_change = int(row["Revenue"]) - previous_monthly_change

        previous_monthly_change = int(row["Revenue"])

        If (monthly_change > increase[1]):
            increase[1] = monthly_change
            increase[0] = row["Date"]

        If (monthly_change < decrease[1]):
            decrease[1] = monthly_change
            decrease[0] = row["Date"]

        monthly_changes.append(int(row["Revenure"]))
    monthly_avg = sum(monthly_change) / len(monthly_change)

Print()
Print()
Print("Financial Analysis")
Print("-------------------------------------------")
Print("Total Months:" + str(total_months))
Print("Total:" + "$" + str(total_revenue))
Print("Average Change:" + "$" + str(round(sum(monthly_change) / len(monthly_change), 2)))
Print("Greatest Increase in Profits:" + str(increase[0]) + "($" + str(increase[1]) + ")")
Print("Greatest Decrease in Profits:" + str(decrease[0]) + "($" + str(decrease[1]) + ")")

output_path = os.path.join('..', '02-Homework', '03-Python', 'Instructions', 'PyBank', 'Output', 'output_budget_data.csv')
with open(output_path, 'w') as csvfile:
    csv.write("Total Months:" + str(total_months))
    csv.write("Total:" + "$" + str(total_revenue))
    csv.write("Average Change:" + "$" + str(round(sum(monthly_change) / len(monthly_change), 2)))
    csv.write("Greatest Increase in Profits:" + str(increase[0]) + "($" + str(increase[1]) + ")")
    csv.write("Greatest Decrease in Profits:" + str(decrease[0]) + "($" + str(decrease[1]) + ")")