input = open('input.txt', 'r').readlines()

inputarray = []
for i in input:
  temparray = []
  x, y = (i.split(','))
  y = y.strip()
  x1, x2 = x.split('-')
  y1, y2 = y.split('-')
  inputarray.append([[int(x1), int(x2)],[int(y1), int(y2)]])
  
jobs = []
counter = 0

for i in inputarray:
  tempjob1 = []
  tempjob2 = []
  for k in range(i[0][0], i[0][1]+1):
    tempjob1.append(k)
  for jo in range(i[1][0], i[1][1]+1):
    tempjob2.append(jo)

  jobs.append([tempjob1, tempjob2])

for i in jobs:
  print(i[0])
  print(i[1])
  print("------")

  for j in i[0]:
    if j in i[1]:
      counter += 1
      break
      
  
  
      
    
      
      

  


print("Counter: ", str(counter))