import re
from functions.validate_potential import validate_potential
from functions.exception_classes import InfoInconsistent
from functions.prefaces import digit_prefaces

def get_digits(digits, line, next_line):
    for preface in digit_prefaces:

        if preface in line and \
            not line.endswith(preface) and \
            not re.findall(r"[^-:\dXx* ]", line[(line.find(preface) + len(preface)):]) and \
            len(line) >= 4 and line[-4:].isdigit(): 
            potential_digits = line[-4:]
            try:
                validate_potential(potential_digits, digits)
            except InfoInconsistent as e:
                raise Exception(f"In validating potential_digits in line, {e} in line: \n\t {line}")
            digits = potential_digits if potential_digits else digits

        if preface in line and \
            line.endswith(preface) and \
            len(next_line) >= 4 and next_line[-4:].isdigit():
            potential_digits = next_line[-4:]
            try:
                validate_potential(potential_digits, digits)
            except InfoInconsistent as e:
                raise Exception(f"In validating potential_digits in next_line, {e} in line: \n\t {next_line}")
            digits = potential_digits if potential_digits else digits

    return digits
