import functions.CONSTANTS as C
from functions.date_patterns import DatePatterns


def check_month_day_year(month, day, year):
    if month.isdigit() and day.isdigit() and year.isdigit() \
        and len(month) == 2 and len(day) == 2 and len(year) == 4 \
            and int(month) < 13 and int(day) < 32 and int(year) < C.MAX_YEAR \
                and int(month) > 0 and int(day) > 0 and int(year) > C.MIN_YEAR:
        return True
    return False


def clean_date(date, index):
    if not date: return ""
    '''
    DatePatterns = [
        0 pattern_day_month_word,
        1 pattern_month_word_day,
        2 pattern_forward_slash,
        3 pattern_date_dash,
        4 pattern_dot
    ]
    '''    
    try: 
        if index == 0: 
            day = date[0].strip(",.")
            month = C.MONTH_DICT[date[1].strip(",.").lower()[:3]] if not date[1].isdigit() else date[1]
            year = date[2]
        else:
            month = C.MONTH_DICT[date[0].strip(".").lower()[:3]] if not date[0].isdigit() else date[0]
            day = date[1].strip(",.")
            year = date[2]
    except Exception as e:
        raise Exception(f"For date '{date}'', \n{e}")
    
    if len(month) == 1: month = "0" + month
    if len(day) == 1: day = "0" + day
    if len(year) == 2: year = "20" + year # assume after 2000

    if not check_month_day_year(month, day, year): 
        raise Exception(f"Pattern {DatePatterns[index]} matched an invalid date: {date}")

    return (".").join([year, month, day])