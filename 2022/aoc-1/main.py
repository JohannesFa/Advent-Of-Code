text = open("input.txt", 'r').readlines()

cals = [[]]

for i in text:
    if i == "\n":
        cals.append([])
    else:
        cal = int(i)
        cals[-1].append(cal)

for i in cals:
    cals[cals.index(i)] = sum(i)

lee = len(cals)
print(sum(sorted(cals)[lee-3:lee]))
