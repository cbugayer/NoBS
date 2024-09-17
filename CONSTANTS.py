import re

MAX_YEAR = 2100
MIN_YEAR = 1900

def check_month_day_year(month, day, year):
    if month.isdigit() and day.isdigit() and year.isdigit() \
        and len(month) == 2 and len(day) == 2 and len(year) == 4 \
            and int(month) < 13 and int(day) < 32 and int(year) < MAX_YEAR \
                and int(month) > 0 and int(day) > 0 and int(year) > MIN_YEAR:
        return True
    return False

NOT_MONTH_DICT = {"Jan": "01", "Feb": "02", "Mar": "03",
              "Apr": "04", "May": "05", "Jun": "06", 
              "Jul" : "07", "Aug": "08", "Sep": "09",
              "Oct": "10", "Nov": "11", "Dec": "12",
              "January": "01", "February": "02", "March": "03",
              "April": "04", "May": "05", "June": "06", 
              "July" : "07", "August": "08", "September": "09",
              "October": "10", "November": "11", "December": "12"}

MONTH_DICT = {"jan": "01", "feb": "02", "mar": "03",
              "apr": "04", "may": "05", "jun": "06",
              "may": "05", "jun": "06", "jul" : "07",
              "aug": "08", "sep": "09", "oct": "10",
              "nov": "11", "dec": "12"}

class InfoNotFound(Exception):
    pass


date_month_word = "[A-Z]{1}[a-z]{2,8}\.? \d{1,2},? \d{2,4}"
pattern_date_month_word = re.compile(date_month_word)
date_forward_slash = "\d{1,2}/\d{1,2}/\d{2,4}"
pattern_date_forward_slash = re.compile(date_forward_slash)





pattern_date_month_word_2 = re.compile(date_month_word + " ?.* ?" + date_month_word)
PATTERNS = [pattern_date_month_word_2]
