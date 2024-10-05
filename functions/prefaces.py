StartPrefaces = ["Beginning Balance on", "Beginning Balance, as of", "Period Start Date:"]
EndPrefaces = ["Ending Balance on", "Ending Balance, as of", "Period End Date:"]

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

DigitPrefaces = regular_case_digit_prefaces + [digit_prefaces.upper() for digit_prefaces in regular_case_digit_prefaces]


midfaces = [" to", " until", " through", " -", "-"]
Midfaces = midfaces + [midface.upper() for midface in midfaces] + [midface.title() for midface in midfaces]

