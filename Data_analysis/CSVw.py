import csv

f = open('output.csv', 'w', newline='')
wr = csv.writer(f)

wr.writerow([1, "A", False])
wr.writerow([2, "B", True])

f.close()
