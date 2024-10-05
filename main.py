
import os
import re
import sys
import fitz
import traceback
import importlib.util
from functions.exception_classes import *

def main():
    
    
    # Define the folders
    txt_folder = 'txt_files'  
    statments_folder = sys.argv[1]  # get the folder path from the command line argument
    cwd = os.getcwd()


    # create a folder to store the text files
    txt_folder_path = fr"{cwd}/{txt_folder}"

    if not os.path.exists(txt_folder_path):
        os.makedirs(txt_folder_path)

    # Loop through the files in the Statements folder and write to the corresponding text files
    for i, filename in enumerate(os.listdir(statments_folder)):
        
        statement_path = f"{statments_folder}/{filename}"  # get document filename
        with fitz.open(statement_path) as doc:  # open document
            text = re.sub(r'\n\s*\n', '\n', chr(12).join([page.get_text() for page in doc]).strip())
        # write as a binary file to support non-ASCII characters
        if text:
            f = open(f"{txt_folder}/{filename[:-4]}.txt", "w")
            f.write(text)
            f.close()

    

    txt_filenames = [f for f in os.listdir(txt_folder_path) if f.endswith('.txt')]
    txt_filenames.sort()
    succeeded, failed, success_list = [], [], []
    for txt_filename in txt_filenames:
        txt_full_path = os.path.join(txt_folder_path, txt_filename)
        
        try:            
            # Dynamically import the .py file as a module
            spec = importlib.util.spec_from_file_location("getInfo.py", "getInfo.py")
            py_file = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(py_file)
            result = py_file.get_info(txt_full_path)
            succeeded.append(txt_filename)
            # If it works, print a success message
            spaces = " " * (30 - len(txt_filename))
            success_list.append(f"{txt_filename}: {spaces} {result}")
        
        except InfoNotFound as e:
            # Handle InfoNotFound errors that occur during method execution
            print(f"INFO NOT FOUND {txt_filename} failed: {e}")
            # print(traceback.format_exc())
            failed.append(txt_filename)
            pass
        except Exception as e:
            # Handle any errors that occur during method execution 
            print(f"EXCEPTION {txt_filename} failed: {e}\n")
            # print(traceback.format_exc())
            failed.append(txt_filename)
            pass
        
    # Print the results
    [print(s) for s in success_list]
    print(f"{len(succeeded)} worked\n")
    print(f"{len(failed)} failed")
    




if __name__ == "__main__":
    main()