
import csv
rows = []
with open("C:\Users\Sri Vishnu Reddy\Downloads\Salary_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
