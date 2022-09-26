import csv

with open('business_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print('pdm run requests', f"\"{row['name']}\"", row['zip_code'])
