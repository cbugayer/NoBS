import functions.CONSTANTS as C
from functions.date import *
from functions.prefaces import *
from functions.validate_potential import validate_potential
from functions.exception_classes import InfoInconsistent


def line_dates(start_date, end_date, line, next_line):
    for index, DATE_PATTERN in enumerate(C.DATE_PATTERNS):
        match_list = [(m[0], m.start(0)) for m in DATE_PATTERN.finditer(line)]

        if not match_list: continue
        try:
            if len(match_list) > 2: raise Exception(f"More than 2 dates on one line - \
                                                {len(match_list)} dates")
        
            if len(match_list) == 2:
                potential_range_start_date = clean_date(match_list[0][0], index)
                potential_range_end_date = clean_date(match_list[1][0], index)
                try: 
                    validate_potential(potential_range_start_date, start_date)
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_range_start_date, \n{e}")
                try:
                    validate_potential(potential_range_end_date, end_date)
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_range_end_date, \n{e}")
                start_date = potential_range_start_date if potential_range_end_date else start_date
                end_date = potential_range_end_date if potential_range_end_date else end_date
                
            for start_preface in start_prefaces:
                potential_preface_start_date = clean_date(preface_2_date(start_preface, line, match_list), index)
                try:
                    validate_potential(potential_preface_start_date, start_date)
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_start_date, \n{e}")
                start_date = potential_preface_start_date if potential_preface_start_date else start_date
                    
            for end_preface in end_prefaces:
                potential_preface_end_date = clean_date(preface_2_date(end_preface, line, match_list), index)
                try:
                    validate_potential(potential_preface_end_date, end_date)
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_end_date, \n{e}")
                end_date = potential_preface_end_date if potential_preface_end_date else end_date

        except Exception as e:
            raise Exception(f"In line: {line}, \n{e} \nusing DATE_PATTERN index = {index}")
    return start_date, end_date 

def next_line_dates(start_date, end_date, line, next_line):
    return start_date, end_date

get_dates_list = [line_dates, next_line_dates]


