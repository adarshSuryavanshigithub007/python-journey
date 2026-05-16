import os

# Specify the directory path
path = "/home/adarshsuryavanshi/"

# Get and print directory contents
contents = os.listdir(path)

print("Directory contents:")
for item in contents:
    print(item)

# Get and print file contents
with open(path + "file.txt", "r") as file:
    print("File contents:")
    print(file.read())