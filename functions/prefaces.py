start_prefaces = ["Beginning Balance on", "Beginning Balance, as of", "Period Start Date:"]
end_prefaces = ["Ending Balance on", "Ending Balance, as of", "Period End Date:"]

regular_case_digit_prefaces = ["Account Number:", 
                  "Account number:", 
                  "Primary Account:", 
                  "Card Number:", 
                #   "Checking", 
                  "CITIBANK PLUS ACCOUNT", 
                  "ending in",
                  "Account #", 
                  "Primary Account Number:",
                  "Account#"]  

digit_prefaces = regular_case_digit_prefaces + [digit_prefaces.upper() for digit_prefaces in regular_case_digit_prefaces]



