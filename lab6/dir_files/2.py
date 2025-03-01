import os

def check_access(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    print(f"Checking access for: {path}\n")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))


specified_path = r"/Users/Acer Aspire lite/pp2/"
check_access(specified_path)
