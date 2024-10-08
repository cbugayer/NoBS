# Changing these would require changing the date regex patterns
MAX_YEAR = 2100
MIN_YEAR = 1900

MONTH_DICT = {"jan": "01", "feb": "02", "mar": "03",
              "apr": "04", "may": "05", "jun": "06",
              "may": "05", "jun": "06", "jul" : "07",
              "aug": "08", "sep": "09", "oct": "10",
              "nov": "11", "dec": "12"}


# These are acceptable characters between the account number preface and the digits
PREFACE2DIGITS = r"[^-:\dXx* ]"
