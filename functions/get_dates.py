from functions.date import *
from functions.prefaces import *
from functions.validate_potential import validate_potential
from functions.exception_classes import InfoInconsistent
from functions.date_patterns import DatePatterns


def preface_2_date(preface, line, match_list):
    before_position = line.find(preface)
    if before_position == -1: return ""
    date_position = before_position + len(preface) + 1 # +1 for space
    for match_obj  in match_list:
        if match_obj.start() == date_position:
            return match_obj.groups()
    return ""

def preface_2_date_next(preface, line, match_list_next):
    if line.endswith(preface):
        if not match_list_next: return ""
        if len(match_list_next) > 1: raise Exception(f"More than 1 dates on next_line - \
                                                {len(match_list_next)} dates")
        return match_list_next[0].groups()
    return ""

def get_dates(start_date, end_date, line, next_line):
    for index, DATE_PATTERN in enumerate(DatePatterns):
        match_list = [m for m in DATE_PATTERN.finditer(line)]
        match_list_next = [m for m in DATE_PATTERN.finditer(next_line)]

        if not match_list and not match_list_next: continue
        try:
            if len(match_list) > 2: raise Exception(f"More than 2 dates on line - \
                                                {len(match_list)} dates")
        
            if len(match_list) == 2:
                potential_range_start_date = clean_date(match_list[0].groups(), index)
                potential_range_end_date = clean_date(match_list[1].groups(), index)
                try: 
                    validate_potential(potential_range_start_date, start_date)
                    start_date = potential_range_start_date if potential_range_end_date else start_date
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_range_start_date, \n{e}")
                try:
                    validate_potential(potential_range_end_date, end_date)
                    end_date = potential_range_end_date if potential_range_end_date else end_date
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_range_end_date, \n{e}")
                
            for start_preface in StartPrefaces:
                potential_preface_start_date = clean_date(preface_2_date(start_preface, line, match_list), index)
                potential_preface_start_date_next = clean_date(preface_2_date_next(start_preface, line, match_list_next), index)
                try:
                    validate_potential(potential_preface_start_date, start_date)
                    start_date = potential_preface_start_date if potential_preface_start_date else start_date
                    validate_potential(potential_preface_start_date_next, start_date)
                    start_date = potential_preface_start_date_next if potential_preface_start_date_next else start_date
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_start_date, \n{e}")
                    
            for end_preface in EndPrefaces:
                potential_preface_end_date = clean_date(preface_2_date(end_preface, line, match_list), index)
                potential_preface_end_date_next = clean_date(preface_2_date_next(end_preface, line, match_list_next), index)
                try:
                    validate_potential(potential_preface_end_date, end_date)
                    end_date = potential_preface_end_date if potential_preface_end_date else end_date
                    validate_potential(potential_preface_end_date_next, end_date)
                    end_date = potential_preface_end_date_next if potential_preface_end_date_next else end_date
                except InfoInconsistent as e:
                    raise Exception(f"In validating potential_end_date, \n{e}")
                
            # Multiple line date range
            if len(match_list) == 1 and len(match_list_next) == 1:

                for midface in Midfaces:
                    midface_after_start = match_list[0].start() + len(match_list[0].group()) == line.find(midface)
                    end_date_at_beginning = match_list_next[0].start() == 0
                    start_date_at_end = match_list[0].end() == len(line)
                    end_date_after_midface = match_list_next[0].start() == len(midface) + 1

                    if (midface_after_start and end_date_at_beginning) or \
                        (start_date_at_end and next_line.startswith(midface) and end_date_after_midface):
                        potential_broken_start_date = clean_date(match_list[0].groups(), index)
                        potential_broken_end_date = clean_date(match_list_next[0].groups(), index)
                        try:
                            validate_potential(potential_broken_start_date, start_date)
                            start_date = potential_broken_start_date if potential_broken_start_date else start_date
                        except InfoInconsistent as e:
                            raise Exception(f"In validating potential_broken_start_date, \n{e}")
                        try:
                            validate_potential(potential_broken_end_date, end_date)
                            end_date = potential_broken_end_date if potential_broken_end_date else end_date
                        except InfoInconsistent as e:
                            raise Exception(f"In validating potential_broken_end_date, \n{e}")

        except Exception as e:
            raise Exception(f"In line: {line}, \n{e} \nusing DATE_PATTERN index = {index}")
        
    return start_date, end_date 




