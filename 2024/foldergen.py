import os, sys
os.chdir(sys.path[0])
print(os.getcwd())
for i in range(1,25):
    dir = f"day-{i}" 
    if not os.path.exists(dir):
        newpath = os.path.join(os.getcwd(),dir)
        print(newpath)
        os.mkdir(newpath)
