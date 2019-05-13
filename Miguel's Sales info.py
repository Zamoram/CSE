import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    fruits_total = 0
    meat_total = 0
    clothes_total = 0
    beverages_total = 0
    office_supplies_total = 0
    for row in reader:
        profits = row[13]
        item_type = row[2]
        if item_type == "Fruits":
            fruits_total += float(profits)
        if item_type == "Meat":
            meat_total += float(profits)
        if item_type == "Clothes":
            clothes_total += float(profits)
        if item_type == "Beverages":
            beverages_total += float(profits)
    print("Fruits", fruits_total)
    print("Meat", meat_total)
    print("Clothes", clothes_total)
    print("Beverages", beverages_total)