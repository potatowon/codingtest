import sys

N = int(input())

frame = [sys.stdin.readline().rstrip( )for _ in range(N)]
conti = True
for r, row in enumerate(frame):
    for c, col in enumerate(row):
        if col == "*":
            head = (r, c)
            conti = False
            break
    if not conti:
        break
heart = (head[0]+1, head[1])
r_arm = frame[heart[0]][heart[1]:].count("*") - 1
l_arm = frame[heart[0]][:heart[1]].count("*")
back = 0
for i in range(heart[0]+1, N):
    if frame[i][heart[1]] == "*":
        back += 1
l_leg = 0
for j in range(heart[0]+1, N):
    if frame[j][heart[1]-1] == "*":
        l_leg +=1
r_leg = 0
for k in range(heart[0]+1, N):
    if frame[k][heart[1] + 1] == "*":
        r_leg +=1
print(heart[0]+1, heart[1]+1)
print(l_arm, r_arm, back, l_leg, r_leg)



