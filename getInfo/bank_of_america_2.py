MONTH_DICT = {"January": "01", "February": "02", "March": "03",
              "April": "04", "May": "05", "June": "06", 
              "July" : "07", "August": "08", "September": "09",
              "October": "10", "November": "11", "December": "12"}

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
                return (".").join([year, MONTH_DICT[month], day.strip(",")])
    raise Exception("Start Date not found")  

def get_end_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Ending balance on"):
                end_date = line.strip("\n ").split(" ")[-3:]
                [month, day, year] = end_date
                return (".").join([year, MONTH_DICT[month], day.strip(",")])
    raise Exception("End Date not found")

def get_account_digits(filepath):
    pass
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Account number:"):
                account_number = line.strip("\n ")[-4:]
                if not account_number.isdigit() or not len(account_number) == 4: raise AssertionError(f"Account Number is not 4 digits:{account_number} (length {len(account_number)})")
                return account_number
    raise Exception("Account Number not found")
    
# print(get_info("PyMuPDFExampleOutputs/bank_of_america_2.txt"))