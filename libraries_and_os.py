# Python RPA Developer Course

# Reading and Writing Files, OS utilities, and Libraries

# first lets define a valid file path 

mypath = r"C:\Users\david\Desktop\new_file.txt"
f = open(mypath, "w")
f.write("HELLO. THIS IS A TEST")
f.close()

import os
# Get current working directory
os.getcwd()
# libraries can have sub-modules

# os.path has functions related to directory and folder paths
os.path.exists(mypath)

# glob is another usefull library for scannign files in folders

# you can use a file path and * to search for every single file type in a folder and have the paths
# returned as individual strings in a python list
import glob

desktop = "C:\Users\david\Desktop\*.txt"
glob.glob(desktop)

for f in glob.glob(desktop):
    print("File Path: %s" % f)
    print("File Contents:")
    print(open(f, "r").read())
