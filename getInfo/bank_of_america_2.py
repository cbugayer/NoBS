import CONSTANTS as C

def get_info(filepath):
        start_date = get_start_date(filepath)
        end_date = get_end_date(filepath)
        account_digits = get_account_digits(filepath)
        return start_date + "-" + end_date + " " + account_digits

def get_start_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Beginning balance on"):
                start_date = line.strip("\n ").split(" ")[-3:]
                [month, day, year] = start_date
                return (".").join([year, C.MONTH_DICT[month], day.strip(",")])
    raise C.InfoNotFound("Start Date not found")  

def get_end_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Ending balance on"):
                end_date = line.strip("\n ").split(" ")[-3:]
                [month, day, year] = end_date
                return (".").join([year, C.MONTH_DICT[month], day.strip(",")])
    raise C.InfoNotFound("End Date not found")

def get_account_digits(filepath):
    pass
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Account number:"):
                account_number = line.strip("\n ")[-4:]
                if not account_number.isdigit() or not len(account_number) == 4: raise AssertionError(f"Account Number is not 4 digits:{account_number} (length {len(account_number)})")
                return account_number
    raise C.InfoNotFound("Account Number not found")
    
# print(get_info("PyMuPDFExampleOutputs/bank_of_america_2.txt"))