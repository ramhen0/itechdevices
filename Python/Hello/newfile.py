import glob

path = "**\*.py"

all_files=[]
for file in glob.glob(path,recursive=True):
    all_files.append(file)
print(all_files)    
