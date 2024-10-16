from functions.get_dates import get_dates
from functions.get_digits import get_digits
from functions.exception_classes import *
from functions.validate_date_range import ValidDateRange


def get_info(text):
    all_lines = text.split("\n")
    all_lines_len = len(all_lines)
    start_date, end_date, account_digits = "", "", ""
    for index, line in enumerate(all_lines):
        next_line = "" if index == all_lines_len - 1 else all_lines[index + 1]
        line = line.strip(" \n")
        next_line = next_line.strip(" \n")
        account_digits = get_digits(account_digits, line, next_line)
        start_date, end_date = get_dates(start_date, end_date, line, next_line)

    error_message = ""
    if not start_date: error_message += "Start Date not found\n"
    if not end_date: error_message += "End Date not found\n"
    if not account_digits: error_message += "Account Number not found\n"
    if error_message: raise InfoNotFound(error_message.rstrip("\n"))
    ValidDateRange(start_date, end_date)
    
    return start_date + "-" + end_date + " " + account_digits