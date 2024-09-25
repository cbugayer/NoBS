import functions.CONSTANTS as C
from functions.exception_classes import InfoInconsistent


def check_month_day_year(month, day, year):
    if month.isdigit() and day.isdigit() and year.isdigit() \
        and len(month) == 2 and len(day) == 2 and len(year) == 4 \
            and int(month) < 13 and int(day) < 32 and int(year) < C.MAX_YEAR \
                and int(month) > 0 and int(day) > 0 and int(year) > C.MIN_YEAR:
        return True
    return False


def check_date_len(date):
    if len(date) != 3: raise Exception(f"Pattern matched an invalid date of len != 3: {date}")


def clean_date(date, index):
    if not date: return ""
    '''
    DATE_PATTERNS = [
        0 pattern_month_word_day,
        1 pattern_day_date_month_word,
        2 pattern_forward_slash,
        3 pattern_date_dash,
        4 pattern_dot
    ]
    '''    
    date_temp = date   
    try: 
        if index < 2: 
            date = date.split(" ")
            check_date_len(date)
            if index == 0:
                month, day, year = C.MONTH_DICT[date[0].strip(".").lower()[:3]], date[1].strip(",."), date[2]
            elif index == 1:
                month, day, year = C.MONTH_DICT[date[1].strip(",.").lower()[:3]], date[0], date[2]
        if index >= 2:
            if index == 2:
                date = date.split("/")
            elif index == 3:
                date = date.split("-")
            elif index == 4:
                date = date.split(".")
            else:
                raise Exception(f"Unknown index {index} of DATE_PATTERNS")
            check_date_len(date)
            month, day, year = date[0], date[1], date[2]
    except Exception as e:
        raise Exception(f"For date '{date_temp}'', \n{e}")
    if len(month) == 1: month = "0" + month
    if len(day) == 1: day = "0" + day
    if len(year) == 2: year = "20" + year # assume after 2000
    if not check_month_day_year(month, day, year): raise Exception(f"Pattern {C.DATE_PATTERNS[index]} matched an invalid date: {date}")
    return (".").join([year, month, day])


