MONTH_DICT = {"Jan": "01", "Feb": "02", "Mar": "03",
              "Apr": "04", "May": "05", "Jun": "06", 
              "Jul" : "07", "Aug": "08", "Sep": "09",
              "Oct": "10", "Nov": "11", "Dec": "12"}

def get_info(filepath):
        start_date = get_start_date(filepath)
        end_date = get_end_date(filepath)
        account_digits = get_account_digits(filepath)
        return start_date + "-" + end_date + " " + account_digits

def get_start_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("PERIOD COVERED BY THIS STATEMENT"):
                start_date = all_lines[index + 1].strip("\n ").split(" ")[:3]
                [month, day, year] = start_date
                return (".").join([year, MONTH_DICT[month.strip(". ")], day.strip(",")])
    raise Exception("Start Date not found")  

def get_end_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("PERIOD COVERED BY THIS STATEMENT"):
                end_date = all_lines[index + 1].strip("\n ").split(" ")[-3:]
                [month, day, year] = end_date
                return (".").join([year, MONTH_DICT[month.strip(". ")], day.strip(",")])
    raise Exception("End Date not found")

def get_account_digits(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Card Number"):
                account_number = all_lines[index + 1].strip("\n ")[-4:]
                if not account_number.isdigit() or not len(account_number) == 4: raise AssertionError(f"Account Number is not 4 digits:{account_number} (length {len(account_number)})")
                return account_number
    raise Exception("Account Number not found")
    
# print(get_info("PyMuPDFExampleOutputs/bmo_1.txt"))