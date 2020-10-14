import csv

with open("msrptrain.csv", 'rt') as input, open('temp.csv', 'wt') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    all = []
    row = next(reader)
    row.insert(0, 'id')
    all.append(row)
    count = 0
    for row in reader:
        row.insert(0, count)
        all.append(row)
        count += 1
    writer.writerows(all)