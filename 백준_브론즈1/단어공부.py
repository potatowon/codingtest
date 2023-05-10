s = input().strip()

s = s.lower()

d = {}

for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

max_value = max(d.values())
max_keys = [k for k, v in d.items() if v == max_value]

if len(max_keys) >= 2:
    print("?")
else:
    print(max_keys[0].upper())


'''
반례 

abcc
'''