import os, sys
os.chdir(sys.path[0])
defualtdir = os.getcwd()
print(defualtdir)
for i in range(1,25+1):

    dir = f"day-{i}" 
    if not os.path.exists(dir):
        newpath = os.path.join(defualtdir,dir)
        print(newpath)
        os.mkdir(newpath)
        os.chdir(newpath)
        with open("part1.py","w+") as a:
            a.write("""#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
            
for i in lines:
    item = i.strip()
""")
        open("input.txt", "w").close()
        open("part2.py", "w").close()
    os.chdir(defualtdir)