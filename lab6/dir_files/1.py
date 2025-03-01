import os

def list_contents(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:")
    print("\n".join(directories) if directories else "No directories found.")
    
    print("\nFiles:")
    print("\n".join(files) if files else "No files found.")
    
    print("\nAll Contents:")
    print("\n".join(os.listdir(path)) if os.listdir(path) else "Directory is empty.")

specified_path = r"/Users/Acer Aspire lite/pp2/"
list_contents(specified_path)
