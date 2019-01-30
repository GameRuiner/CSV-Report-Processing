import sys
import csv

from date_parse import date_parsing
from state_parse import state_parsing

number_of_args = len(sys.argv)

if number_of_args == 1:
    file_name = 'test.csv'
    file_write_name = 'output.csv'
elif number_of_args == 2:
    file_name = sys.argv[1]
    file_write_name = 'output.csv'
elif number_of_args == 3:
    file_name = sys.argv[1]
    file_write_name = sys.argv[2]
else:
    sys.exit("Wrong file name")


try:
    file_object = open(file_name, "r", encoding='utf8')
except FileNotFoundError:
    sys.exit("File not found " + file_name)
try:
    reader = file_object.readlines()
except UnicodeDecodeError:
    sys.exit("'utf-8' codec can't decode " + file_name)

file_to_write = open(file_write_name, 'w', newline='')
result_csv = csv.writer(file_to_write, delimiter=',', lineterminator="\n")

rows_to_write = []
for row in reader:
    current_row = row.strip().split(",")
    if len(current_row) != 4:
        print("Parsing error " + row, file=sys.stderr)
        continue
    current_row_to_write = []

    date = date_parsing(current_row[0])
    if date != "err":
        current_row_to_write.append(date)
    else:
        continue

    current_row_to_write.append(state_parsing(current_row[1]))

    current_row_to_write.append(current_row[2])

    current_row_to_write.append(int(float(current_row[3][:-1]) / 100 * int(current_row[2])))

    rows_to_write.append(current_row_to_write)
    #result_csv.writerow(current_row_to_write)

rows_to_write.sort(key=lambda x: x[1])
rows_to_write.sort(key=lambda x: x[0])

for row in rows_to_write:
    result_csv.writerow(row)


