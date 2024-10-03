from functions.get_dates import get_dates
from functions.get_digits import get_digits
from functions.exception_classes import InfoNotFound

def get_info(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        all_lines_len = len(all_lines)
        start_date, end_date, account_digits = "", "", ""
        for index, line in enumerate(all_lines):
            next_line = "" if index == all_lines_len - 1 else all_lines[index + 1]
            line = line.strip(" \n")
            next_line = next_line.strip(" \n")
            account_digits = get_digits(account_digits, line, next_line)
            start_date, end_date = get_dates(start_date, end_date, line, next_line)

        error_message = ""
        if not start_date: error_message += "\nStart Date not found"
        if not end_date: error_message += "\nEnd Date not found"
        if not account_digits: error_message += "\nAccount Number not found"
        if error_message: raise InfoNotFound(error_message + "\n")
        if start_date == end_date: raise Exception("Start Date and End Date are the same", start_date)
    
    return start_date + "-" + end_date + " " + account_digits