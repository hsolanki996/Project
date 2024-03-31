import os
import shutil
from tkinter import Tk, filedialog

def organize_files(files):
    for file_path in files:
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            file_extension = file_name.split('.')[-1].lower()
            destination_dir = f"{file_extension}_files"
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_dir, file_name))
            print(f"Moved '{file_name}' to '{destination_dir}'")
        else:
            print(f"'{file_path}' is not a file.")

def main():
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    root.destroy()
    
    if not files:
        print("No files selected.")
        return

    organize_files(files)

if __name__ == "__main__":
    main()