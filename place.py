import copy

f = open("input.txt", "r")
lines = f.readlines()
n = lines[0].replace("\n", "")
p = lines[1].replace("\n", "")
s = lines[2].replace("\n", "")
scooter_loc = []
scot = int(s)
for i in range(0, scot * 12):
    scooter_loc.append(lines[i + 3].replace("\n", "").split(","))

f.close()


rows = int(n[0])
columns = int(n[0])
w, h = rows, columns;
grid = [[0.0 for x in range(h)] for y in range(w)]
for i in range(rows-1,-1,-1):
    for j in range(0,columns,1):
        for k in range(0,scot*12,1):
            if i==int(scooter_loc[k][0])-1 and j==int(scooter_loc[k][1])-1:
                grid[i][j] = float("-inf")




