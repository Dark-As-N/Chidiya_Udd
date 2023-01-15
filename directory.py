# Python program to explain os.listdir() method
	
# importing os module
import os
import random

# Get the list of all files and directories
# in the root directory

path = r"C:\Users\91865\syntax_error\photos"
dir_list = os.listdir(path)
print("Files and directories in the photos folder :")

# print the list
print(dir_list)

for i in range(100):
    print(random.choice(dir_list))
