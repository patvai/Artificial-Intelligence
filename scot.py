import sys
from collections import Counter

f = open("input3.txt", "r")
lines = f.readlines()
n = lines[0].replace("\n", "")
num = int(n)
print(num)

if num > 15:
    sys.exit()



p = lines[1].replace("\n", "")
print(p)

s = lines[2].replace("\n", "")
print(s)

scooter_loc = []
scot = int(s)
for i in range(1,scot+1):
    print("J",(i))
for i in range(0, scot * 12):
    scooter_loc.append(lines[i + 3].replace("\n", "").split(","))
print(scooter_loc)

a = [scooter_loc]


frequency_list = Counter(tuple((i)) for i in a[0])

print("bigram","frequency")
for key,val in frequency_list.items():

    print(key, val)




f.close()
