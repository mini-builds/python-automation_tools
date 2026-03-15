
"""
Folder Backup Script
Author: Mini_builds
Description: Creates a timestamped backup of a folder.
"""


import os 
import shutil
from datetime import datetime

source_folder= input("Enter folder path to backup: ")
backup_location=input("Enter backup destination: ")
date= datetime.now().strftime("%Y_%m_%d")

if not os.path.exists(source_folder):
    print("Source folder does not exist")
    exit()
    
backup_folder=os.path.join(backup_location,f"backup_{date}")
os.makedirs(backup_folder,exist_ok=True)

print("Backup folder created:",backup_folder)
copied_file=0
skipped_folder=0
for item in os.listdir(source_folder):

    source_path = os.path.join(source_folder, item)
    destination_path = os.path.join(backup_folder, item)
    
    if os.path.isfile(source_path):

        shutil.copy2(source_path, destination_path)
        copied_file+=1
        print(f"Copied: {item}")
        
    else:
        skipped_folder+=1
        
print("\n ---Backup summary---")
print("Copied files:",copied_file)
print("Folders skipped:",skipped_folder)