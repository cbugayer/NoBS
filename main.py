import importlib.util
import os
import traceback
import functions.exception_classes as C

import getInfo as gi

def main():
            
    # Define the folders
    txt_folder_path = 'PyMuPDFExampleOutputs'  

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
        
        except C.InfoNotFound as e:
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