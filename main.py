import importlib.util
import os
import traceback
import CONSTANTS as C
from collections import defaultdict

import getInfo as gi

def main():
            
    # Define the folders
    py_folder_path = 'getInfo' 
    txt_folder_path = 'PyMuPDFExampleOutputs'  

    txt_filenames = [f for f in os.listdir(txt_folder_path) if f.endswith('.txt')]
    py_filenames = [f for f in os.listdir(py_folder_path) if f.endswith('.py') and f != "__init__.py"]
    txt_filenames.sort()
    py_filenames.sort()
    py_to_txt = defaultdict(list)

    for txt_filename in txt_filenames:
        txt_full_path = os.path.join(txt_folder_path, txt_filename)
        was_successful = False 
        for py_filename in py_filenames:
            if os.stat(os.path.join(py_folder_path, py_filename)).st_size == 0: continue
            try:
                py_full_path = os.path.join(py_folder_path, py_filename)
                
                # Dynamically import the .py file as a module
                spec = importlib.util.spec_from_file_location(py_filename[:-3], py_full_path)
                py_file = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(py_file)
                if py_filename == "citi_2.py" and txt_filename == "citi_1.txt": 
                    print(f"Running {py_filename} on {txt_filename}")
                
                result = py_file.get_info(txt_full_path)
                py_to_txt[py_filename].append(txt_filename)
                # If it works, print a success message
                matching_filename = py_filename.split(".")[0] == txt_filename.split(".")[0]
                # if matching_filename: 
                #     print(f"MATCH: {py_filename} executed successfully for {txt_filename} with result: {result}")
                # else:
                #     print(f"NON-MATCH: {py_filename} executed successfully for {txt_filename} with result: {result}")
                # if was_successful: 
                #     print(f"!!      Another file worked for {txt_filename}")
                was_successful = True
            
            except C.InfoNotFound as e:
                # Handle InfoNotFound errors that occur during method execution
                if py_filename == "citi_2.py" and txt_filename == "commerce.txt": 
                    print(f"{py_filename} did not execute on {txt_filename}: {e}")
                    # print(traceback.format_exc())
                pass
            except Exception as e:
                # Handle any errors that occur during method execution
                print(f"{py_filename} did not execute on {txt_filename}: {e}\n")
                print(traceback.format_exc())
                pass


        # if no .py files work
        if not was_successful:
            # UNCOMMENT
            # print(f"No .py files executed successfully for {txt_filename}\n")
            continue
        # else:
        #     print("\n")
        
    # Print the results
    sorted_py_to_txt_keys = sorted(py_to_txt.keys())
    for py_filename in sorted_py_to_txt_keys:
        working_txt = py_to_txt[py_filename]
        print(f"{len(working_txt)} {py_filename} worked on: {working_txt}")




if __name__ == "__main__":
    main()