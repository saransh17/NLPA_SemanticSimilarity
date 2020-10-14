import csv
reader = csv.reader(open("msrptrain.csv"))
reader1 = csv.reader(open("msrptest.csv"))
f = open("combined.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()