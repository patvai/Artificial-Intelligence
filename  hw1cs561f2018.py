

f = open("input.txt", "r")
lines = f.readlines()
n = lines[0].replace("\n", "")
num = int(n)
print(num)





p = lines[1].replace("\n", "")
print(p)

po = int(p)

s = lines[2].replace("\n", "")
print(s)

scooter_loc = []
scot = int(s)

for i in range(0, scot * 12):

    scooter_loc.append(lines[i + 3].replace("\n", "").split(","))
        # numbers_float = list(map(int, lines[i+3].replace("\n", "").split(",")))
print(scooter_loc)
t = []
d = {}
for x, y in scooter_loc:
   d[x, y] = d.get((x,y), 0) + 1
for key, val in d.items():
    piy = [key, val]
    t.append(piy)




print(t)
gem = sorted(t, key=lambda x: x[1], reverse=True)
#pit = sorted(t, key=lambda x: x[2], reverse=True)
#print(pit)
print(gem)
act = 0
count = 0
#kili = [x[0] for x in gem]
for i in gem:
    kili = [x[0] for x in gem]
    kilo = [x[1] for x in gem]
act = act + kilo[1]
count = count + 1
if count == po:
    f1 = open("output.txt", 'w')
    print >>f1, act











