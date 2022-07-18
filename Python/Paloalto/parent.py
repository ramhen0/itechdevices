import glob
import os

#import zeus

older_name=os.path.basename(os.getcwd())
#This
path=os.getcwd()+"\\"+ zeus_file[:-9]+ "*.py"
#file[:-10] gets ride of last 10 characters with are \parent.py
print(zeus_file[:-10]+ " Parent Intialized...")
#path = "**/*.py"


all_files=[]

for file in glob.glob(path):
    all_files.append(file)


for file in all_files:
    file_name_strip=os.path.basename(file)
    if file_name_strip != "parent.py":
        exec(open(file).read())
