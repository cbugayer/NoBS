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
        if start_date == end_date: raise Exception("Start Date and End Date are the same", start_date)
    
    return start_date + "-" + end_date + " " + account_digits

def check_for_range_dates(line, next_line):
    for index, date_pattern in enumerate(C.DATE_PATTERNS):
        match_list = date_pattern.findall(line)
        if len(match_list) == 2:
            start_date = C.clean_date(match_list[0], index)
            end_date = C.clean_date(match_list[1], index)
            return True, True, start_date, end_date
    return False, False, None, None

def check_for_start_date(line, next_line):
    # for index, date_pattern in enumerate(C.DATE_PATTERNS):
    #     match_list = date_pattern.findall(line)
    #     if len(match_list) == 1:
    #         start_date = C.clean_date(match_list[0], index)
    #         return True, start_date
    return False, None
    

def check_for_end_date(line, next_line):
    # for index, date_pattern in enumerate(C.DATE_PATTERNS):
    #     match_list = date_pattern.findall(line)
    #     if len(match_list) == 1:
    #         end_date = C.clean_date(match_list[0], index)
    #         return True, end_date
    return False, None


def check_for_account_digits(line, next_line):
    for check in C.DIGIT_CHECKS:
        account_digits = check(line, next_line)
        if account_digits: return True, account_digits 
    return False, None

