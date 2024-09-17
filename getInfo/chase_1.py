import re
import CONSTANTS as C

def get_info(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        got_start, got_end, got_account = False, False, False
        all_lines_len = len(all_lines)
        for index, line in enumerate(all_lines):
            next_line = "" if index == all_lines_len - 1 else all_lines[index + 1]
            line = line.strip(" \n")
            next_line = next_line.strip(" \n")
            # This looks messy - probably will not break anyway (check all lines)
            if not (got_start and got_end): [got_start, got_end, start_date, end_date] = check_for_range_dates(line, next_line)
            if not got_start: [got_start, start_date] = check_for_start_date(line, next_line)
            if not got_end: [got_end, end_date] = check_for_end_date(line, next_line)
            if not got_account: [got_account, account_digits] = check_for_account_digits(line, next_line)
            if got_start and got_end and got_account: break
        error_message = ""
        if not got_start: error_message += "\nStart Date not found"
        if not got_end: error_message += "\nEnd Date not found"
        if not got_account: error_message += "\nAccount Number not found"
        if error_message: raise C.InfoNotFound(error_message + "\n")
    
    return start_date + "-" + end_date + " " + account_digits


def clean_date(date):
    date = date.split(" ")
    if len(date) != 3: raise Exception("Pattern matched an invalid date: " + date)
    month, day, year = C.MONTH_DICT[date[0].strip(".").lower()[:3]], date[1].strip(",."), date[2]
    if len(day) == 1: day = "0" + day
    if len(year) == 2: year = "20" + year
    if not C.check_month_day_year(month, day, year): raise Exception("Pattern matched an invalid date: " + date)
    return (".").join([year, month, day])

def check_for_range_dates(line, next_line):
    pattern = C.pattern_date_month_word
    match_list = pattern.findall(line)
    if len(match_list) == 2:
        start_date = clean_date(match_list[0])
        end_date = clean_date(match_list[1])
        return True, True, start_date, end_date
    return False, False, None, None

def check_for_start_date(line, next_line):
    pattern = C.pattern_date_month_word
    match_list = pattern.findall(line)
    if len(match_list) == 1:
        start_date = clean_date(match_list[0])
        return True, start_date
    return False, None
    

def check_for_end_date(line, next_line):
    pattern = C.pattern_date_month_word
    match_list = pattern.findall(line)
    if len(match_list) == 1:
        end_date = clean_date(match_list[0])
        return True, end_date
    return False, None

def check_for_account_digits(line, next_line):
    if line.startswith("Primary Account:"):
        account_digits = line.split(" ")[-1]
        account_digits = account_digits[-4:]
        if len(account_digits) != 4 or not account_digits.isdigit(): raise Exception("Pattern matched an invalid account number: " + account_digits)
        return True, account_digits
    return False, None

