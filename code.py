import os
import shutil
source = input("Enter source folder ")
destination = input("Destination folder name ")
source = source + "/"
destination = destination + "/"
list_of_file = os.listdir(source)

for file in list_of_file:
    shutil.copy((source+file),destination)