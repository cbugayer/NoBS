import re

# Changing these would require changing the date regex patterns
MAX_YEAR = 2100
MIN_YEAR = 1900

def clean_date(date, index):
    if not date: return ""
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

MONTH_DICT = {"jan": "01", "feb": "02", "mar": "03",
              "apr": "04", "may": "05", "jun": "06",
              "may": "05", "jun": "06", "jul" : "07",
              "aug": "08", "sep": "09", "oct": "10",
              "nov": "11", "dec": "12"}

class InfoNotFound(Exception):
    pass
class InfoInconsistent(Exception):
    pass

month = "(?:0?[1-9]|1[0-2])"
day = "(?:0?[1-9]|[12][0-9]|3[01])"
year = "(?:19[0-9]{2}|20[0-9]{2}|[0-9]{2})" # 1900-2099
month_word = "[A-Z]{1}[a-z]{2,8}\.?"

date_month_word_day = f"{month_word} {day},? {year}"
pattern_month_word_day = re.compile(date_month_word_day)

date_forward_slash = fr"{month}/{day}/{year}"
pattern_forward_slash = re.compile(date_forward_slash)

date_dash = f"{month}-{day}-{year}"
pattern_dash = re.compile(date_dash)

date_day_month_word = f"{day} {month_word} {year}"
pattern_day_month_word = re.compile(date_day_month_word)


DATE_PATTERNS = [pattern_month_word_day, pattern_forward_slash, pattern_dash, pattern_day_month_word]

start_prefaces = ["Beginning Balance on "]
end_prefaces = ["Ending Balance on "]



def line_digits(line, next_line):
    if len(line) >= 4 and line[-4:].isdigit() and \
    (line.startswith("Primary Account:") and line != "Primary Account:") or \
    ("Account Number:" in line and not line.endswith("Account Number:")) or \
    ("citibank plus account" in line.lower() and line != "citibank plus account"):
        return line[-4:]
    return None

def next_line_digits(line, next_line):
    if len(next_line) >= 4 and next_line[-4:].isdigit() and \
    (line == "Checking") or \
    (line.endswith("Primary Account Number:")):
        return next_line[-4:]
    return None
    
DIGIT_CHECKS = [line_digits, next_line_digits] 


# def check_for_start_date(line, next_line):
#     commerce = line.find("Beginning Balance on ")
#     if commerce != -1 and 