def get_info(filepath):
        start_date = get_start_date(filepath)
        end_date = get_end_date(filepath)
        account_digits = get_account_digits(filepath)
        return start_date + "-" + end_date + " " + account_digits

def get_start_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Statement Period:"):
                start_date = line.strip("\n ").split(" ")[-3]
                [month, day, year] = start_date.split("/")
                return (".").join([year, month, day])
    raise Exception("Start Date not found")  

def get_end_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Statement Period:"):
                end_date = line.strip("\n ").split(" ")[-1]
                [month, day, year] = end_date.split("/")
                return (".").join([year, month, day])
    raise Exception("End Date not found")

def get_account_digits(filepath):
    pass
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Checking"):
                account_number = all_lines[index + 1].strip("\n ")[-4:]
                if not account_number.isdigit() or not len(account_number) == 4: raise AssertionError(f"Account Number is not 4 digits:{account_number} (length {len(account_number)})")
                return account_number
    raise Exception("Account Number not found")
    
# print(get_info("PyMuPDFExampleOutputs/becu_1.txt"))