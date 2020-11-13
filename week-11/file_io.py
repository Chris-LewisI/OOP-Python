# AUTHOR: Chris Ibraheem

# Import pathlib and shutil modules
import pathlib
import shutil

# Create a path object that represents your current working directory
cwd_path = pathlib.Path.cwd()
# Print out your current directory's path
print(cwd_path)

# Referencing the current working directory path object, create a new path object that will be used to create a new folder.  The new folder is to be called "folder_week11".
week11_path = cwd_path/"folder_week11"
# Create a new directory using the path created in the prior step.
week11_path.mkdir()

# Using the path that was created to make the "folder_week11" directory, create a path that will be used to create text file.  The name of the test file will be "week11.txt"
txt_path = week11_path/"week11.txt"
# Use the method to create the "week11.txt" file as a blank file.
txt_path.touch()

# Create a string variable that will be used to write the following text to the "week_11.txt" text file: "Test: Writing to file."
string_variable = "Test: Writing to file."
txt_path.write_text(string_variable)
# Print out the the file contents (using the read() method) to confirm that text was written.
print(txt_path.read_text())

# Make a new path in the folder_week11 directory and call it "file_backups"
backups_path = week11_path/"file_backups"
# Make a new directory referencing the new path created in the prior step.
backups_path.mkdir()

# Using the shutil module, make copy of the week11.txt file, called "week11_backup.txt" and save it in the file_backups directory.
shutil.copy(txt_path, backups_path)

# Navigate back to the folder_week11 directory
# From the folder_week11 directory, use rglob() method to print out only the txt files that have been created in this directory and the subdirectories. There should only be two files.
for file in week11_path.rglob("*.txt"):
    print(file)