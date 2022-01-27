import os, glob

path = "*.fna"
dirs = os.listdir( path )
command = f"rgi main -i {file_name} -o ./rgiresults{file_name} -d wgs --clean"

for file_name in dirs:
    os.system(command)