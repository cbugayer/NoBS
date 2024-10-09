import os

# def add_suffix(statement_path, destination):
#     base, ext = os.path.splitext(destination)
#     counter = 1

#     # Keep adding (1), (2), ... until a unique name is found
#     while os.path.exists(destination) or statement_path == destination:
#         destination = f"{base}({counter}) {ext}"
#         counter += 1

#     return destination

def add_suffix(statement_path, destination):
    # Separate the directory, base name, and extension (if it's a file)
    directory, name = os.path.split(destination)
    base, ext = os.path.splitext(name)
    
    counter = 1
    new_path = destination

    # Keep adding (1), (2), ... until a unique file/folder name is found
    while os.path.exists(new_path):
        if ext:  # It's a file
            new_name = f"{base} ({counter}){ext}"
        else:  # It's a folder (no extension)
            new_name = f"{name} ({counter})"
        
        new_path = os.path.join(directory, new_name)
        counter += 1

    return new_path

