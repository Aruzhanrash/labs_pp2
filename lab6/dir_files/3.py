import os

def test_path(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    print(f"The specified path exists: {path}\n")
    print("Directory portion:", os.path.dirname(path))
    print("Filename portion:", os.path.basename(path))


specified_path = r"/Users/Acer Aspire lite/pp2/"
test_path(specified_path)