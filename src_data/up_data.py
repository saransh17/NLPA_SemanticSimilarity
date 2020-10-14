import csv

with open('msrp_test.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split('\t') for line in stripped if line)
    with open('msrptest.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('#1 ID', '#2 ID','#1 String','#2 String','Quality'))
        writer.writerows(lines)