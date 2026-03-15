import csv
import os

input_file=input("Enter csv fil path: ")
output_file="clean_data.csv"

with open (input_file,"r",newline="",encoding="utf-8") as file:
    reader=csv.reader(file)
    rows=list(reader)
    
    if not os.path.exists(input_file):
        print("File does not exist")
        exit()
    
cleaned_rows=[]
empty_rows=0

rows_cleaned=0

header = rows[0]
clean_header = [h.strip().title() for h in header]

cleaned_rows.append(clean_header)

for row in rows[1:]:
    cleaned_row=[]
    if not any(cell.strip() for cell in row):
            empty_rows+=1
           
            continue
  
    for cell in row:
        cell=cell.strip()
        
        cell=cell.capitalize()
        
        cleaned_row.append(cell)
        
        
    cleaned_rows.append(cleaned_row)
    rows_cleaned+=1

    
with open (output_file,"w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerows(cleaned_rows)

print("Cleaned csv saved as:", output_file)
print(f"Rows skipped:{empty_rows}")
print(f"Rows cleaned:{rows_cleaned}")   
