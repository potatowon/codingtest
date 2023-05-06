
n, k = map(int, input().split())
num = n
kay = k
up = 1
down = 1
for i in range(k):
    up *= num
    num -= 1

for j in range(k):
    down *= kay
    kay -= 1

print(up//down)