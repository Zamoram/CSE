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
    middle_east_and_north_africa_total = 0
    australia_and_oceania_total = 0
    europe_total = 0
    asia_total = 0
    central_america_and_the_caribbean_total = 0
    north_america_total = 0
    fruit_unit_total = 0
    meat_unit_total = 0
    clothes_unit_total = 0
    beverages_unit_total = 0
    office_supplies_unit_total = 0
    cosmetics_unit_total = 0
    snacks_unit_total = 0
    personal_care_unit_total = 0
    household_unit_total = 0
    vegetables_unit_total = 0
    baby_food_unit_total = 0
    cereal_unit_total = 0
    for row in reader:
        profits = row[13]
        units_sold = row[8]
        item_type = row[2]
        region = row[0]
        if item_type == "Fruits":
            fruits_total += float(profits)
            fruit_unit_total += int(units_sold)
        if item_type == "Meat":
            meat_total += float(profits)
            meat_unit_total += int(units_sold)
        if item_type == "Clothes":
            clothes_total += float(profits)
            clothes_unit_total += int(units_sold)
        if item_type == "Beverages":
            beverages_total += float(profits)
            beverages_unit_total += int(units_sold)
        if item_type == "Office Supplies":
            office_supplies_total += float(profits)
            office_supplies_unit_total += int(units_sold)
        if item_type == "Cosmetics":
            cosmetics_total += float(profits)
            cosmetics_unit_total += int(units_sold)
        if item_type == "Snacks":
            snacks_total += float(profits)
            snacks_unit_total += int(units_sold)
        if item_type == "Personal Care":
            personal_care_total += float(profits)
            personal_care_unit_total += int(units_sold)
        if item_type == "Household":
            household_total += float(profits)
            household_unit_total += int(units_sold)
        if item_type == "Vegetables":
            vegetables_total += float(profits)
            vegetables_unit_total += int(units_sold)
        if item_type == "Baby Food":
            baby_food_total += float(profits)
            baby_food_unit_total += int(units_sold)
        if item_type == "Cereal":
            cereal_total += float(profits)
            cereal_unit_total += int(units_sold)
        if region == "Sub-Saharan Africa":
            sub_saharan_africa_total += float(profits)
        if region == "Middle East and North Africa":
            middle_east_and_north_africa_total += float(profits)
        if region == "Australia and Oceania":
            australia_and_oceania_total += float(profits)
        if region == "Europe":
            europe_total += float(profits)
        if region == "Asia":
            asia_total += float(profits)
        if region == "Central America and the Caribbean":
            central_america_and_the_caribbean_total += float(profits)
        if region == "North America":
            north_america_total += float(profits)

    print("Fruits", fruits_total, fruit_unit_total)
    print("Meat", meat_total, meat_unit_total)
    print("Clothes", clothes_total, clothes_unit_total)
    print("Beverages", beverages_total, beverages_unit_total)
    print("Office Supplies", office_supplies_total, office_supplies_unit_total)
    print("Cosmetics", cosmetics_total, cosmetics_unit_total)
    print("Snacks", snacks_total, snacks_unit_total)
    print("Personal Care", personal_care_total, personal_care_unit_total)
    print("Household", household_total, household_unit_total)
    print("Vegetables", vegetables_total, vegetables_unit_total)
    print("Baby Food", baby_food_total, baby_food_unit_total)
    print("Cereal", cereal_total, cereal_unit_total)
    print("Sub-Saharan Africa", sub_saharan_africa_total)
    print("Middle East and South Africa", middle_east_and_north_africa_total)
    print("Australia and Oceania", australia_and_oceania_total)
    print("Europe", europe_total)
    print("Asia", asia_total)
    print("Central America and the Caribbean", central_america_and_the_caribbean_total)
    print("North America", north_america_total)
item_type = ['Fruits', 'Meat', ' Clothes', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks',
             'Personal Care', 'Household', 'Vegetables', 'Baby Food', 'Cereal']
profit_list = [fruits_total, meat_total, clothes_total, beverages_total, office_supplies_total, cosmetics_total,
             snacks_total, personal_care_total, household_total, vegetables_total, baby_food_total, cereal_total]
highest_profit = max(profit_list)
print(highest_profit)
highest_index = profit_list.index(highest_profit)
print(item_type[highest_index])
region = ['Sub-Saharan Africa', 'Middle East and North Africa', 'Australia and Oceania', 'Europe',
          'Asia', 'Central America and the Caribbean', 'North America']
profit_list = [sub_saharan_africa_total, middle_east_and_north_africa_total, australia_and_oceania_total,
               europe_total, asia_total, central_america_and_the_caribbean_total, north_america_total]
highest_profit = max(profit_list)
print(highest_profit)
highest_index = profit_list.index(highest_profit)
print(region[highest_index])

fruit_average = fruits_total / fruit_unit_total
meat_average = meat_total / meat_unit_total
clothes_average = clothes_total / clothes_unit_total
beverages_average = beverages_total / beverages_unit_total
office_supplies_average = office_supplies_total / office_supplies_unit_total
cosmetics_average = cosmetics_total / cosmetics_unit_total
snacks_average = snacks_total / snacks_unit_total
personal_care_average = personal_care_total / personal_care_unit_total
household_average = household_total / household_unit_total
vegetables_average = vegetables_total / vegetables_unit_total
baby_food_average = baby_food_total / baby_food_unit_total
cereal_average = cereal_total / cereal_unit_total

print("Fruit",  fruit_average)
print("Meat", meat_average)
print("Clothes", clothes_average)
print("Beverages", beverages_average)
print("Office Supplies", office_supplies_average)
print("Cosmetics", cosmetics_average)
print("Snacks", snacks_average)
print("Personal Care", personal_care_average)
print("Household", household_average)
print("Vegetables", vegetables_average)
print("Baby Food", baby_food_average)
print("Cereal", cereal_average)

item_type = ['Fruits', 'Meat', ' Clothes', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks',
             'Personal Care', 'Household', 'Vegetables', 'Baby Food', 'Cereal']
highest_average_list = [fruit_average, meat_average, clothes_average, beverages_average, office_supplies_average,
                          cosmetics_average, snacks_average, personal_care_average, household_average,
                          vegetables_average, baby_food_average, cereal_average]
highest_average_profit = max(highest_average_list)
print(highest_average_profit)
highest_average_index = highest_average_list.index(highest_average_profit)
print(item_type[highest_average_index])
