import sys


def date_parsing(date):
    list_date = date.split("/")
    if len(list_date) != 3:  # check date format
        print("Error in parsing date " + date, file=sys.stderr)
        return "err"
    return list_date[2] + "-" + list_date[0] + "-" + list_date[1]
