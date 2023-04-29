s = input().strip()
k = input().strip()
new_s = []
for i in s:
    if not i.isdigit():
        new_s.append(i)
new_s = ''.join(new_s)
if k in new_s:
    print(1)
else:
    print(0)