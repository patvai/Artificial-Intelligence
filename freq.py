from collections import Counter

a = [(['7', '8'], ['4', '7'],['3', '4'],['3', '8'],['4', '8'],['3','4'],['7','8'],['8','7'],['4','3'])]

frequency_list = Counter(tuple((i)) for i in a[0])

print("bigram","frequency")
for key,val in frequency_list.items():
    print(key, val)