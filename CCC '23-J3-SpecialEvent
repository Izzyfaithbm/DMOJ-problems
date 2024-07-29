n = int(input())

points = [0, 0, 0, 0, 0]

for _ in range(n):
    full = list(input())
    for i in range(len(full)):
        if full[i] == 'Y':
            points[i] += 1

maxValue = 0
maxDay = 0

for i in range(len(points)):
    if points[i] > maxValue:
        maxValue = points[i]
        maxDay = i+1

numOfMax = 0 

for i in range(len(points)):
    if points[i] == maxValue:
        numOfMax+=1

if numOfMax == 1:
    print(maxDay)
else:
    days = []
    for i in range(len(points)):
        if points[i] == maxValue:
            days.append(i+1)
    print(','.join(map(str,days)))
