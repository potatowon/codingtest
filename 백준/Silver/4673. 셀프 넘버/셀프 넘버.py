self_num = [True]*10001

for i in range(1, 10001):
    d = i + sum([int(j) for j in str(i)])
    if d <= 10000:
        self_num[d] = False

# print(self_num)
for k in range(1, 10001):
    if self_num[k]:
        print(k)