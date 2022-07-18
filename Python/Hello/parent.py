

# child.py will be replaced by generic file name. I need to find the name of all the files and have them in a list and then
# place them in between open()
#for x in range(1,3):
#this will go through all the files in the give folder including the file that executes all the all_files
#so it is possible that we might create an infinite loop
#to avoid that we can create if statement to loopover
#    exec(open("child"+str(x)+".py").read())


import glob

path = "**\*.py"

all_files=[]
for file in glob.glob(path,recursive=True):
    all_files.append(file)

for file in all_files:
    if file != "parent.py":
        exec(open(file).read())
