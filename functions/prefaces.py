StartPrefaces = ["Beginning Balance on", "Beginning Balance, as of", "Period Start Date:"]
EndPrefaces = ["Ending Balance on", "Ending Balance, as of", "Period End Date:"]

regular_case_digit_prefaces = ["Account Number:", 
                  "Account number:", 
                  "Primary Account:", 
                  "Card Number:", 
                  "CITIBANK PLUS ACCOUNT", 
                  "ending in",
                  "Account #", 
                  "Primary Account Number:",
                  "Account#"]  

DigitPrefaces = regular_case_digit_prefaces + [digit_prefaces.upper() for digit_prefaces in regular_case_digit_prefaces]


midfaces = ["to", "until", "through", "-"]
midfaces_spaces = [m + " " for m in midfaces] + [" " + m for m in midfaces] + ["-"]
Midfaces = midfaces_spaces + [midface.upper() for midface in midfaces_spaces] + [midface.title() for midface in midfaces_spaces]

