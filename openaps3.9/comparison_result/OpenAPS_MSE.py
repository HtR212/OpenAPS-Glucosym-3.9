import csv
import os
import sys

patient_num = sys.argv[1]
directory = f"patient{patient_num}"
se = 0
counter = 0
for filename in os.listdir(directory):
    with open(f"{directory}/{filename}") as aps_reader:
        csv_reader = csv.reader(aps_reader)
        header = True
        for row in csv_reader:
            if header:
                header = False
                continue
            counter += 1
            se += (float(row[1])-float(row[3]))**2
        aps_reader.close()
with open(f"mse_openaps.csv", "a", newline='') as mse_writer:
    csv_writer = csv.writer(mse_writer)
    csv_writer.writerow([patient_num, se/counter])
    mse_writer.close()
