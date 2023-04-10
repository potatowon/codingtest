a = int(input())
b = int(input())
c = int(input())    

num = list(str(a*b*c))
n_num = [0]*10
for n in num:
    n_num[int(n)] += 1

for idx in n_num:
    print(idx)