import re
import CONSTANTS as C


def get_info(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        got_start, got_end, got_account = False, False, False
        all_lines_len = len(all_lines)
        got_start, got_end, got_account = False, False, False
        for index, line in enumerate(all_lines):
            next_line = "" if index == all_lines_len - 1 else all_lines[index + 1]
            if not got_start: [got_start, start_date] = check_for_start_date(line, next_line)
            if not got_end: [got_end, end_date] = check_for_end_date(line, next_line)
            if not got_account: [got_account, account_digits] = check_for_account_digits(line, next_line)
            if got_start and got_end and got_account: break
        error_message = ""
        if not got_start: error_message += "\nStart Date not found\n"
        if not got_end: error_message += "End Date not found\n"
        if not got_account: error_message += "Account Number not found\n"
        if error_message: raise Exception(error_message)
    
    return start_date + "-" + end_date + " " + account_digits

def check_for_start_date(line, next_line):
    pattern = re.compile(r"(19|20)\d{2}.*?(19|20)\d{2}")
    try:
        if pattern.search(line):
            start_date = line.strip(" \n").split(" ")[:3]
            [month, day, year] = [C.MONTH_DICT[start_date[0]], start_date[1].strip(",."), start_date[2]]
            return True, (".").join([year, month, day])
    except Exception as e:
        return False, None
    return False, None
    

def check_for_end_date(line, next_line):
    pattern = re.compile(r"(19|20)\d{2}.*?(19|20)\d{2}")
    try:
        if pattern.search(line):
            end_date = line.strip(" \n").split(" ")[4:7]
            [month, day, year] = [C.MONTH_DICT[end_date[0]], end_date[1].strip(",."), end_date[2]]
            return True, (".").join([year, month, day])
    except Exception as e:
        return False, None
    return False, None

def check_for_account_digits(line, next_line):
    if "ending in" in line.lower():
        account_digits = line.strip(" \n").split(" ")[-1]
        return True, account_digits
    return False, None

# print(get_info("PyMuPDFExampleOutputs/capital_one_1.txt"))
# print(get_info("PyMuPDFExampleOutputs/chase_4.txt"))
