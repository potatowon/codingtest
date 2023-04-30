s = input().strip()

s = s.lower()

d = {}

for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1


