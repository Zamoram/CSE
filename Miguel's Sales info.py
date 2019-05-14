import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    fruits_total = 0
    meat_total = 0
    clothes_total = 0
    beverages_total = 0
    office_supplies_total = 0
    cosmetics_total = 0
    snacks_total = 0
    personal_care_total = 0
    household_total = 0
    vegetables_total = 0
    baby_food_total = 0
    cereal_total = 0
    sub_saharan_africa_total = 0
    for row in reader:
        profits = row[13]
        item_type = row[2]
        region = row[0]
        if item_type == "Fruits":
            fruits_total += float(profits)
        if item_type == "Meat":
            meat_total += float(profits)
        if item_type == "Clothes":
            clothes_total += float(profits)
        if item_type == "Beverages":
            beverages_total += float(profits)
        if item_type == "Office Supplies":
            office_supplies_total += float(profits)
        if item_type == "Cosmetics":
            cosmetics_total += float(profits)
        if item_type == "Snacks":
            snacks_total += float(profits)
        if item_type == "Personal Care":
            personal_care_total += float(profits)
        if item_type == "Household":
            household_total += float(profits)
        if item_type == "Vegetables":
            vegetables_total += float(profits)
        if item_type == "Baby Food":
            baby_food_total += float(profits)
        if item_type == "Cereal":
            cereal_total += float(profits)
        if region
    print("Fruits", fruits_total)
    print("Meat", meat_total)
    print("Clothes", clothes_total)
    print("Beverages", beverages_total)
    print("Office Supplies", office_supplies_total)
    print("Cosmetics", cosmetics_total)
    print("Snacks", snacks_total)
    print("Personal Care", personal_care_total)
    print("Household", household_total)
    print("Vegetables", vegetables_total)
    print("Baby Food", baby_food_total)
    print("Cereal", cereal_total)
item_type = ['Fruits', 'Meat', ' Clothes', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks',
             'Personal Care', 'Household', 'Vegetables', 'Baby Food', 'Cereal']
profit_list = [fruits_total, meat_total, clothes_total, beverages_total, office_supplies_total, cosmetics_total,
             snacks_total, personal_care_total, household_total, vegetables_total, baby_food_total, cereal_total]
highest_profit = max(profit_list)
print(highest_profit)
highest_index = profit_list.index(highest_profit)
print(item_type[highest_index])

