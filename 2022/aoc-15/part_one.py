
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = open('input.txt', 'r').readlines()
test = False
if test:
    text = open('testinput.txt', 'r').readlines()
for i in range(len(text)):
    text[i] = text[i].strip()


