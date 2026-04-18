import os
import csv


for sales in os.listdir('data'):
    with open(f'data/{sales}', newline='') as infile, open('pink_morsel_sales.csv', 'w', newline='') as outfile:

        # DictReader reads the first line as the header
        reader = csv.DictReader(infile)
        for row in reader:
            # only interested in pink morsels
            if row['product'] != "pink morsel":
                continue

            sales = float(row['quantity']) * float(row['price'][1:])

            # write to output file
            writer = csv.writer(outfile)
            writer.writerow([sales, row['date'], row['region']])
