import sys
from collections import defaultdict

p, m = map(int, input().split())

players = []
for _ in range(p):
    l, n = input().split()
    players.append((int(l), n))

# 각 방의 정보를 저장할 리스트. 각 방은 (레벨의 최소값, 레벨의 최대값, 플레이어 목록)의 형태로 저장됩니다.
rooms = defaultdict(list)
idx = 0
for player in players:
    l, n = player
    added = False
    for k, v in rooms.items():
        if v[0][0] - 10 <= l <= v[0][0] + 10 and len(v) < m:
            rooms[k].append((l, n))
            added = True
            break
    if not added:
        idx += 1
        rooms[idx].append((l, n))

for k, v in rooms.items():
    if len(v) == m:
        print('Started!')
    else:
        print("Waiting!")
    v.sort(key=lambda x : x[1])
    for l, n in v:
        print(l, n)







