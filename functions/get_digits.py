from functions.validate_potential import validate_potential
from functions.exception_classes import InfoInconsistent

def line_digits(digits, line, next_line):
    if len(line) >= 4 and line[-4:].isdigit() and \
    (line.startswith("Primary Account:") and line != "Primary Account:") or \
    ("Account Number:" in line and not line.endswith("Account Number:")) or \
    ("citibank plus account" in line.lower() and line.lower() != "citibank plus account"):
        potential_digits = line[-4:]
        try:
            validate_potential(potential_digits, digits)
        except InfoInconsistent as e:
                raise Exception(f"In validating potential_digits in line, {e} in line: \n\t {line}")
        digits = potential_digits if potential_digits else digits
    return digits


def next_line_digits(digits, line, next_line):
    if len(next_line) >= 4 and next_line[-4:].isdigit() and \
    (line == "Checking") or \
    (line.endswith("Primary Account Number:")):
        potential_digits = next_line[-4:]
        try:
            validate_potential(potential_digits, digits)
        except InfoInconsistent as e:
                raise Exception(f"In validating potential_digits in next_line, {e} in line: \n\t {line}")
        digits = potential_digits if potential_digits else digits
    return digits

get_digits_list = [line_digits, next_line_digits]