import re
MONTH_DICT = {"Jan": "01", "Feb": "02", "Mar": "03",
              "Apr": "04", "May": "05", "Jun": "06", 
              "Jul" : "07", "Aug": "08", "Sep": "09",
              "Oct": "10", "Nov": "11", "Dec": "12",
              "January": "01", "February": "02", "March": "03",
              "April": "04", "May": "05", "June": "06", 
              "July" : "07", "August": "08", "September": "09",
              "October": "10", "November": "11", "December": "12"}

class InfoNotFound(Exception):
    pass


date_month_word = "[A-Z]{1}[a-z]{2,8}\.? \d{1,2},? \d{2,4}"
pattern_date_month_word = re.compile(date_month_word)





pattern_date_month_word_2 = re.compile(date_month_word + " ?.* ?" + date_month_word)
PATTERNS = [pattern_date_month_word_2]
