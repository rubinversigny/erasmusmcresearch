import os, glob

# Open a file
path = "*.txt"
dirs = os.listdir( path )

for file_name in dirs:
    string_to_add = (CARD_/RESfinder_/NCBI_)
    print(string_to_add)
    with open(path + file_name, 'r') as f:
        lines = f.readlines()
    lines = [string_to_add + line for line in lines]
    with open(path + file_name, 'w') as f:
        f.writelines(lines)
