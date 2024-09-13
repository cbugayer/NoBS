import importlib.util
import os

import getInfo as gi

def main():
            
    # Dynamically import the .py file as a module
    py_folder_path = "getInfo"
    txt_files = ["PyMuPDFExampleOutputs/capital_one_1.txt", "PyMuPDFExampleOutputs/ally_1.txt"]
    py_files = ["capital_one_1.py"]
    for txt_filename in txt_files:
        for py_filename in py_files:
            try:
                py_full_path = os.path.join(py_folder_path, py_filename)
                spec = importlib.util.spec_from_file_location(py_filename[:-3], py_full_path)
                py_file = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(py_file)
                success_result = py_file.get_info(txt_filename)
                print(f"SUCCESS: {py_filename} executed successfully for {txt_filename} with result: {success_result}\n")
            except Exception as e:
                # Handle any errors that occur during method execution
                print(f"FAILURE: capital_one_1 did not execute on {txt_filename}: {e}")
                pass




if __name__ == "__main__":
    main()