import os 

folder=input("Enter folder path: ")
prefix=input("Enter filename prefix: ")

files=sorted(os.listdir(folder))
counter=1
print("\nPreview\n")

for file in files:
    old_path=os.path.join(folder,file)
    
    if os.path.isfile(old_path):
        
        name,ext=os.path.splitext(file)
        
        new_name=f"{prefix}_{counter}{ext}"
        
        new_path= os.path.join(folder,new_name)
        
        print(f"{file} -> {new_name}")
        
        counter+=1
        
confirm= input("\n Proceed with renaming? (Yes/No): ")

if confirm=="yes":
    counter=1
    rename_count=0
    skipped_count=0
    
    if os.path.isdir(old_path):
        print(f"Skipping folder: {file}")
        skipped_count+=1
    
    for file in files:
         old_path = os.path.join(folder, file)

         if os.path.isfile(old_path):

            name, ext = os.path.splitext(file)

            new_name = f"{prefix}_{counter}{ext}"
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)

            counter += 1
            rename_count+=1
    print("\nRenaming complete\n")
    print(f"Total renamed files: {rename_count}")
    print(f"Total skipped folders:{skipped_count} ")
    
else:
    print("\nOperation cancelled.")