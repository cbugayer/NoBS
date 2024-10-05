from functions.exception_classes import InvalidDateRange

def ValidDateRange(start_date, end_date):
    if start_date == end_date: raise InvalidDateRange(f"Start Date {start_date} and End Date {end_date} are the same")
    start_year, start_month, start_day = [int(time) for time in start_date.split(".")]
    end_year, end_month, end_day = [int(time) for time in end_date.split(".")]
    if (start_year > end_year) or \
       (start_year == end_year and start_month > end_month) or \
       (start_year == end_year and start_month == end_month and start_day > end_day): 
        raise InvalidDateRange(f"Start Date {start_date} is after End Date {end_date}")