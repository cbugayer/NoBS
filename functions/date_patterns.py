import re 

month = "(?:0?[1-9]|1[0-2])"
day = "(?:0?[1-9]|[12][0-9]|3[01])"
year = "(?:19[0-9]{2}|20[0-9]{2}|[0-9]{2})" # 1900-2099
month_word = "[A-Z]{1}[a-z]{2,8}\.?"

date_month_word_day = f"{month_word} {day},? {year}"
pattern_month_word_day = re.compile(date_month_word_day)

date_forward_slash = f"{month}/{day}/{year}"
pattern_forward_slash = re.compile(date_forward_slash)

date_dash = f"{month}-{day}-{year}"
pattern_dash = re.compile(date_dash)

date_day_month_word = f"{day} {month_word} {year}"
pattern_day_month_word = re.compile(date_day_month_word)

date_dot = fr"{month}\.{day}\.{year}"
pattern_dot = re.compile(date_dot)


Date_Patterns = [pattern_month_word_day, pattern_day_month_word, pattern_forward_slash, pattern_dash, pattern_dot]