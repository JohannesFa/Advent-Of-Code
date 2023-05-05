input = open('input.txt', 'r').readlines()
list_of_inputs = []
for line in input:
  templist = []
  one, two = line.split(' ')
  templist.append(one.strip())
  templist.append(two.strip())
  list_of_inputs.append(templist)

yumovedic = {'x': 1, 'y': 2, 'z': 3}
winlosedicx = {'a': 3, 'b': 0, 'c': 6}
winlosedicy = {'a': 6, 'b': 3, 'c': 0}
winlosedicz = {'a': 0, 'b': 6, 'c': 3}
winlosedica = {'x': 'z', 'y': 'x', 'z': 'y'}
winlosedicb = {'x': 'x', 'y': 'y', 'z': 'z'}
winlosedicc = {'x': 'y', 'y': 'z', 'z': 'x'}
translate = {'a':'x', 'b':'y','c':'z'}
whatdic = {'x': winlosedicx, 'y': winlosedicy, 'z': winlosedicz}
whatdicabc = {'a': winlosedica, 'b': winlosedicb, 'c': winlosedicc}
#x lose, y tie, z win
def getpoints(opmove, yumove):
  temppoints = 0

  tempdic2 = whatdicabc[opmove.lower()]
  yumove = tempdic2[yumove.lower()]
  
  tempdic = whatdic[yumove.lower()]
  temppoints += tempdic[opmove.lower()]

  temppoints += yumovedic[yumove.lower()]
  
  return temppoints
  
#A for Rock, B for Paper, and C for Scissors

points = 0

for i in list_of_inputs:
  points += getpoints(i[0], i[1])

print(points)
