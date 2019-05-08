import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    for row in reader:
        old_number = row[13]
        print(old_number)
        new_row = row[2]
        
        print(new_row)
