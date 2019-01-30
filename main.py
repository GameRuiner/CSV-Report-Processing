import sys
import csv

from date_parse import date_parsing
from state_parse import state_parsing

number_of_args = len(sys.argv)

# check number of args for naming files for work
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


# set file for reading
try:
    file_object = open(file_name, "r", encoding='utf8')
except FileNotFoundError:
    sys.exit("File not found " + file_name)
try:
    reader = file_object.readlines()
except UnicodeDecodeError:
    sys.exit("'utf-8' codec can't decode " + file_name)


# file for writing, with separator "," and newline "\n" (Unix newline)
file_to_write = open(file_write_name, 'w', newline='')
result_csv = csv.writer(file_to_write, delimiter=',', lineterminator="\n")

# list of rows for sorting them
rows_to_write = []
for row in reader:  # row in reading file
    current_row = row.strip().split(",")
    if len(current_row) != 4:
        print("Parsing error " + row, file=sys.stderr)
        continue
    current_row_to_write = []

    # parsing and adding date
    date = date_parsing(current_row[0])
    if date != "err":
        current_row_to_write.append(date)
    else:
        continue

    # finding country to state in state_parsing and adding to row
    current_row_to_write.append(state_parsing(current_row[1]))

    # adding number of impressions
    current_row_to_write.append(current_row[2])

    # calculating and adding number of clicks
    current_row_to_write.append(int(float(current_row[3][:-1]) / 100 * int(current_row[2])))

    # saving row for sorting
    rows_to_write.append(current_row_to_write)

# sorting rows lexicographically by date followed by the country code
rows_to_write.sort(key=lambda x: x[1])
rows_to_write.sort(key=lambda x: x[0])

# writing to output file
for row in rows_to_write:
    result_csv.writerow(row)


