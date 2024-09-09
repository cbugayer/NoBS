def get_info(filepath):
        start_date = get_start_date(filepath)
        end_date = get_end_date(filepath)
        account_digits = get_account_digits(filepath)
        return start_date + "-" + end_date + " " + account_digits

def get_start_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            if line.startswith("Beginning Balance, as of"):
                start_date = line.strip("\n ").split(" ")[-1]
                [month, day, year] = start_date.split("/")
                return (".").join([year, month, day])
    raise Exception("Start Date not found")  

def get_end_date(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for index, line in enumerate(all_lines):
            if line.startswith("Ending Balance, as of"):
                end_date = line.strip("\n ").split(" ")[-1]
                [month, day, year] = end_date.split("/")
                return (".").join([year, month, day])
    raise Exception("End Date not found")

def get_account_digits(filepath):
    with open(filepath, "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            if line.startswith("Account Number:"):
                account_number = line.strip("\n ")[-4:]
                return account_number
    raise Exception("Account Number not found")
    
# print(get_info("PyMuPDFExampleOutputs/ally_1.txt"))