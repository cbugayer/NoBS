
import os
import re
import sys
import fitz
import shutil
import traceback
import importlib.util
from functions.exception_classes import *


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <statements_folder_path>")
        sys.exit(1)

    statements_folder_path = sys.argv[1] 
    is_file = os.path.isfile(statements_folder_path)

    if not os.path.exists(statements_folder_path):
        print(f"Path {statements_folder_path} does not exist")
        sys.exit(1)

    if is_file:
        dirpath, single_file = os.path.split(statements_folder_path)
        parent_folder_path = os.path.dirname(statements_folder_path)
        pdf_files = [single_file]
        processed_folder_path = parent_folder_path
    else:
        dirpath, _, pdf_files = next(os.walk(statements_folder_path))
        parent_folder_path = os.path.dirname(os.path.dirname(dirpath))
        statements_folder_name = os.path.basename(dirpath.rstrip("/"))

        processed_folder_path = os.path.join(parent_folder_path, f"RENAMED_{statements_folder_name}")
        logs_file_path = os.path.join(parent_folder_path, f"LOGS_{statements_folder_name}.txt")

        if not os.path.exists(processed_folder_path): os.makedirs(processed_folder_path)

    success_list, failure_list = [], []
    # Loop through the files in the statements folder
    for filename in pdf_files:
        result = filename[:-4]
        spaces = " " * (40 - len(filename))

        statement_path = os.path.abspath(os.path.join(dirpath, filename))  # get document filename
        with fitz.open(statement_path) as doc:  # open document
            text = re.sub(r'\n\s*\n', '\n', chr(12).join([page.get_text() for page in doc]).strip())

        try:            
        # Dynamically import the getInfo.py file as a module
            spec = importlib.util.spec_from_file_location("getInfo.py", "getInfo.py")
            py_file = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(py_file)

            # Result
            result = py_file.get_info(text)
            success_list.append(f"{filename}: {spaces} {result}\n")
    
        except InfoNotFound as e:
            # # Handle InfoNotFound errors that occur during method execution
            # print(f"INFO NOT FOUND {filename} failed: {e}")
            # print(traceback.format_exc())
            failure_list.append(f"{filename}: {spaces} failed\n")
            pass
        except Exception as e:
            # # Handle any errors that occur during method execution 
            # print(f"EXCEPTION {filename} failed: {e}\n")
            # print(traceback.format_exc())
            failure_list.append(f"{filename}: {spaces} failed\n")
            pass

        if statement_path != os.path.join(processed_folder_path, f"{result}.pdf"):
            shutil.copy(statement_path, os.path.join(processed_folder_path, f"{result}.pdf"))

    # Print the results   
    if is_file:    
        print("Worked!\n", success_list[0].strip("\n")) if success_list else print("Failed!\n", failure_list[0].strip("\n"))
    else:
        success_list.sort()
        with open(logs_file_path, "w") as f:
            [f.write(s) for s in success_list]
            f.write("\n")
            [f.write(k) for k in failure_list]

        print(f"{len(success_list)} worked")
        print(f"{len(failure_list)} failed")

    
if __name__ == "__main__":
    main()