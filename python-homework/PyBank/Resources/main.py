import os

import csv

col_list = ["Date", "Profit/Losses"]

with open('/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    file = open('/Resources/budget_data.csv')
    reader = csv.reader(file)
    lines = len(list(reader))
#def count_months(csv_reader):
    #months = int(csv_file[0])




   # print(f'Processed {line_count} lines.')





