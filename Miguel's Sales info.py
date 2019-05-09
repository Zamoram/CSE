import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    for row in reader:
        Profits = row[13]
        item_type = row[2]
        0 += Profits
        if item_type == "Fruits":
            print(item_type, Profits)