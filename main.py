import camelot
import pandas as pd

def extract_table(file_path):
    tables = camelot.read_pdf(file_path, flavor='stream', pages='0')
    df = pd.DataFrame()
    for table in tables:
        df = pd.concat([df, table.df], ignore_index=True)
    return df