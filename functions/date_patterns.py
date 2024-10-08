import re 


month = r"(0?[1-9]|1[0-2])"
day = r"(0?[1-9]|[12][0-9]|3[01])"
year = r"(19[0-9]{2}|20[0-9]{2}|[0-9]{2})" # 1900-2099
month_word = r"([A-Z]{1}[a-z]{2,8}\.?)"


date_month_word_day = fr"{month_word} {day},? {year}"
pattern_month_word_day = re.compile(date_month_word_day)

date_forward_slash = fr"{month}/{day}/{year}"
pattern_forward_slash = re.compile(date_forward_slash)

date_dash = fr"{month}-{day}-{year}"
pattern_dash = re.compile(date_dash)

date_day_month_word = fr"{day} {month_word} {year}"
pattern_day_month_word = re.compile(date_day_month_word)

date_dot = fr"{month}\.{day}\.{year}"
pattern_dot = re.compile(date_dot)


DatePatterns = [pattern_day_month_word, pattern_month_word_day, pattern_forward_slash, pattern_dash, pattern_dot]