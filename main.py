import os
import csv


for sales in os.listdir('data'):
    with open(f'data/{sales}', newline='') as infile, open('data/pink_morsel_sales.csv', 'w', newline='') as outfile:

        reader = csv.DictReader(infile) # DictReader reads the first line as the header
        writer = csv.writer(outfile)
        writer.writerow(['sales', 'date', 'region']) # write the header for the output file
        for row in reader:
            # only interested in pink morsels
            if row['product'] != "pink morsel":
                continue

            sales = float(row['quantity']) * float(row['price'][1:])

            writer.writerow([sales, row['date'], row['region']])
