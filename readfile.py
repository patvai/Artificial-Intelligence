f = open("input.txt","r")
lines = f.readlines()
n = lines[0].replace("\n", "")
p = lines[1].replace("\n", "")
s = lines[2].replace("\n", "")
scooter_loc = []
scot = int(s)
for i in range(0, scot*12):
    scooter_loc.append(lines[i+3].replace("\n", "").split(","))
   

f.close()
