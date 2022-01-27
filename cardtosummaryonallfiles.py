import os, glob

# Open a file
path = "D:/500genomes/rgiresultsklebsiella/"
dirs = os.listdir( path )

for file_name in dirs:
    message_count = file_name
    string_to_add = (message_count) + ('_rgi \t')
    print(string_to_add)
    with open(path + file_name, 'r') as f:
        lines = f.readlines()
    lines = [string_to_add + line for line in lines]
    with open(path + file_name, 'w') as f:
        f.writelines(lines)

with open($outfilepath$/resultsCARD.txt, "wb") as outfile:
    for file_name in read_files:
        with open(path + file_name, 'r') as infile:
            outfile.write(infile.read())