import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    total = 0
    for row in reader:
        profits = row[13]
        item_type = row[2]
        if item_type == "Fruits" and "Meat":
            print(item_type, profits)
            total += float(profits)
    print(total)