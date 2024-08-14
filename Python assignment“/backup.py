import shutil 
from datetime import date 
import os 
def copy_files(source_dir, dest_dir):
     if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
     if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Destination directory '{dest_dir}' created.")
        
     files=os.listdir(source_dir)
     for fname in files:
         shutil.copy(os.path.join(source_dir,fname),dest_dir)


source_dir = str(input("Enter path of  source directory :"))
dest_dir = str(input("Enter path of destination directory :"))
copy_files(source_dir, dest_dir)