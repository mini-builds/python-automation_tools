Smart File Organizer (Python)

This is a Python automation script that organizes files inside a folder based on file type.

Features
- Automatically sorts files into folders like Images, Videos, Documents, etc.
- Preview mode (Dry Run) to see changes before executing
- Handles duplicate filenames safely
- Logs all operations in a log file
- File categories can be customized using file_type.json

How to Run

1. Run the script:

python file_organiser.py

2. Enter the folder path you want to organize.

3. Choose mode:
1 = Preview Mode (shows what will happen)
2 = Execute Mode (moves the files)

Configuration

File types and categories are defined in the file_type.json file.
You can edit this file to add or modify file categories.

Example

photo.jpg → Images/photo.jpg  
video.mp4 → Videos/video.mp4  
document.pdf → Documents/document.pdf

Author:Mini_builds
Python automation project for file management.