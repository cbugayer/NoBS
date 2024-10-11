
import os
import re
import sys
import fitz
import shutil
import traceback
import importlib.util
from functions.exception_classes import *
from functions.destination_suffix import add_suffix


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <statements_folder_path>")
        sys.exit(1)

    log = False
    if len(sys.argv) == 3 and sys.argv[2] == "log":
        log = True
        

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
        parent_folder_path = os.path.dirname(dirpath)
        statements_folder_name = os.path.basename(dirpath.rstrip("/"))

        processed_folder_path = os.path.join(parent_folder_path, f"RENAMED_{statements_folder_name}")
        logs_file_path = os.path.join(parent_folder_path, f"LOGS_{statements_folder_name}.txt")

        processed_folder_path = processed_folder_path if not os.path.exists(processed_folder_path) else add_suffix("", processed_folder_path)
        logs_file_path = logs_file_path if not os.path.exists(logs_file_path) else add_suffix("", logs_file_path)
        os.makedirs(processed_folder_path)

    success_list, failure_list, failure_description_list = [], [], []
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
            if log: failure_description_list.append(f"{'-' * 40}\nFILENAME:\n{filename}\n\nERROR:\n{e}\n\nTEXT:\n{text}\n\n")
            pass
        except Exception as e:
            # # Handle any errors that occur during method execution 
            # print(f"EXCEPTION {filename} failed: {e}\n")
            # print(traceback.format_exc())
            failure_list.append(f"{filename}: {spaces} failed\n")
            if log: failure_description_list.append(f"{'-' * 40}\nFILENAME:\n{filename}\n\nERROR:\n{e}\n\nTEXT:\n{text}\n\n")
            pass
        
        destination_path = os.path.join(processed_folder_path, f"{result}.pdf")
        if os.path.exists(destination_path) or statement_path == destination_path:
            destination_path = add_suffix(statement_path, destination_path)
        
        shutil.copy(statement_path, destination_path)

    # Print the results   
    if is_file:    
        print("Worked!\n", success_list[0].strip("\n")) if success_list else print("Failed!\n", failure_list[0].strip("\n"))
    else:
        success_list.sort()
        with open(logs_file_path, "w") as f:
            [f.write(s) for s in success_list]
            f.write("\n")
            [f.write(k) for k in failure_list]
            f.write("\n\n")
            [f.write(j) for j in failure_description_list]

        print(f"{len(success_list)} worked")
        print(f"{len(failure_list)} failed")

    
if __name__ == "__main__":
    main()