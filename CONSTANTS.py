import re

# Changing these would require changing the date regex patterns
MAX_YEAR = 2100
MIN_YEAR = 1900

def clean_date(date, index):
    # DATE_PATTERNS = [pattern_month_word_day, pattern_forward_slash, pattern_date_dash, pattern_day_date_month_word]
    if index == 0:
        date = date.split(" ")
        if len(date) != 3: raise Exception("Pattern matched an invalid date: " + date)
        month, day, year = MONTH_DICT[date[0].strip(".").lower()[:3]], date[1].strip(",."), date[2]
    elif index == 1:
        date = date.split("/")
        if len(date) != 3: raise Exception("Pattern matched an invalid date: " + date)
        month, day, year = date[0], date[1], date[2]
    elif index == 2:
        date = date.split("-")
        if len(date) != 3: raise Exception("Pattern matched an invalid date: " + date)
        month, day, year = date[0], date[1], date[2]
    elif index == 3:
        date = date.split(" ")
        if len(date) != 3: raise Exception("Pattern matched an invalid date: " + date)
        month, day, year = MONTH_DICT[date[1].strip(",.").lower()[:3]], date[0], date[2]

    if len(month) == 1: month = "0" + month
    if len(day) == 1: day = "0" + day
    if len(year) == 2: year = "20" + year
    if not check_month_day_year(month, day, year): raise Exception(f"Pattern {DATE_PATTERNS[index]} matched an invalid date: {date}")
    return (".").join([year, month, day])

def check_month_day_year(month, day, year):
    if month.isdigit() and day.isdigit() and year.isdigit() \
        and len(month) == 2 and len(day) == 2 and len(year) == 4 \
            and int(month) < 13 and int(day) < 32 and int(year) < MAX_YEAR \
                and int(month) > 0 and int(day) > 0 and int(year) > MIN_YEAR:
        return True
    return False

# NOT_MONTH_DICT = {"Jan": "01", "Feb": "02", "Mar": "03",
#               "Apr": "04", "May": "05", "Jun": "06", 
#               "Jul" : "07", "Aug": "08", "Sep": "09",
#               "Oct": "10", "Nov": "11", "Dec": "12",
#               "January": "01", "February": "02", "March": "03",
#               "April": "04", "May": "05", "June": "06", 
#               "July" : "07", "August": "08", "September": "09",
#               "October": "10", "November": "11", "December": "12"}

MONTH_DICT = {"jan": "01", "feb": "02", "mar": "03",
              "apr": "04", "may": "05", "jun": "06",
              "may": "05", "jun": "06", "jul" : "07",
              "aug": "08", "sep": "09", "oct": "10",
              "nov": "11", "dec": "12"}

class InfoNotFound(Exception):
    pass

month = "(?:0?[1-9]|1[0-2])"
day = "(?:0?[1-9]|[12][0-9]|3[01])"
year = "(?:19[0-9]{2}|20[0-9]{2}|[0-9]{2})" # 1900-2099
month_word = "[A-Z]{1}[a-z]{2,8}\.?"

# date_month_word = "[A-Z]{1}[a-z]{2,8}\.? \d{1,2},? \d{2,4}"
date_month_word_day = f"{month_word} {day},? {year}"
pattern_month_word_day = re.compile(date_month_word_day)

date_forward_slash = fr"{month}/{day}/{year}"
pattern_forward_slash = re.compile(date_forward_slash)

date_day_month_word = f"{day} {month_word} {year}"
pattern_day_month_word = re.compile(date_day_month_word)

date_dash = f"{month}-{day}-{year}"
pattern_dash = re.compile(date_dash)

DATE_PATTERNS = [pattern_month_word_day, pattern_forward_slash, pattern_dash, pattern_day_month_word]


# sw_ = starts with
# ne_ = not entirely
# e_ = entirely

def sw_ne_primary_account(line, next_line):
    return line.startswith("Primary Account:") and line != "Primary Account:", line
def sw_ne_account_number(line, next_line):
    return "Account Number:" in line and not line.endswith("Account Number:"), line
def e_checking(line, next_line):
    return line == "Checking" and next_line[-4:].isdigit(), next_line
def ne_bank_plus_account(line, next_line):
    return "citibank plus account" in line.lower() and line != "citibank plus account" and line[-4:].isdigit(), line


PRE_ACCOUNT_NUMBER_CHECKS = [sw_ne_primary_account, sw_ne_account_number, e_checking, ne_bank_plus_account]