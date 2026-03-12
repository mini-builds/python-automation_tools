import os
import shutil
import json 

"""
Smart File Organizer
Author: Mini_builds
Description: Organizes files in a folder based on file type with preview mode and duplicate protection.
"""

def get_unique_filename(destination):
                  # destination = os.path.join(target_folder, filename)

                   base, extension = os.path.splitext(destination)
                   counter = 1

                   while os.path.exists(destination):
                     destination = f"{base}_{counter}{extension}"
                     counter += 1
                   return destination

def write_log(message):
    with open("organizer_log.txt", "a",encoding="utf-8") as log:
        log.write(message + "\n")
        
        
def file_type_load():
     
       try:  
         with open("file_type.json","r") as file:
          return json.load(file)
         
       except FileNotFoundError:
        print("Error: file_type.json not found")
       return {}
           
def organize_folder(folder_path,mode):
    
    if not os.path.exists(folder_path):
        print("folder does not exist")
        return
   
    file_types=file_type_load()
    moved_files=0
    skipped_files=0
    total_files=0
    
    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path,filename)
        
        if os.path.isdir(file_path):
            skipped_files+=1
            continue
        total_files+=1
        moved=False
        
        for folder_name,extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder=os.path.join(folder_path,folder_name)
            

            
                if not os.path.exists(target_folder):
                     os.makedirs(target_folder)
                destination = os.path.join(target_folder, filename)

                destination = get_unique_filename(destination)
                if mode=="1":
                    print(f"[PREVIEW] {filename:<35}-->{folder_name}/{os.path.basename(destination)}")
                    moved=True
                    break 
               
                else:      
                  try:
                     
                       shutil.move(file_path,destination) 
                       message = f"Moved: {filename}->{destination}"
                       print(message)
                       write_log(message)
                       moved_files+=1
                       moved=True
                       break
                  except Exception as e:
                       print(f"Error moving{filename}:{e}")

        if not moved:
                 Others_folder=os.path.join(folder_path,"Others")
                 if not os.path.exists(Others_folder):
                    os.makedirs(Others_folder)
                 if mode=="1":
                    print(f"[PREVIEW] {filename:<35}-->{Others_folder}")
                  
                 else:    
                  try:
                      destination = os.path.join(Others_folder, filename)
                      destination = get_unique_filename(destination)
                      shutil.move(file_path, destination)
                 
                      message = f"Moved: {filename} → {Others_folder}"
                      print(message)
                      write_log(message)

                      moved_files += 1
                
                   
                  except Exception as e:
                   error_msg = f"Error moving {filename}: {e}"
                   print(error_msg)
                   write_log(error_msg)    
    
    print("\n--- Summary ---")
    print(f"Total files scanned: {total_files}")
    print(f"Files moved        : {moved_files}")
    print(f"Folders skipped    : {skipped_files}")
           
if __name__=="__main__":
    path=input("enter folder path here:")
    print("Select Mode")
    print("1-PREVIEW(DRY RUN)")
    print("2-EXECUTE")
    
    mode=input("Enter choice(1 or 2): ")
    organize_folder(path,mode)