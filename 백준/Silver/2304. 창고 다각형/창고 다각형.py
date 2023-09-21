import sys

n = int(input()) # 기둥의 개수
storage = []
max_x = 0
max_l = 0
idx = 0
for _ in range(n):
    x, l = map(int, sys.stdin.readline().split()) # 위치, 높이
    storage.append((x, l))
storage.sort(key=lambda x: x[0]) # 위치 순서로 정렬
# 최고점 찾기
max_height = 0
max_index = 0
for i in range(n):
    if storage[i][1] > max_height:
        max_height = storage[i][1]
        max_index = i


## 최고점 기준으로 왼쪽은 증가만, 오른쪽은 감소만 해야한다.

area = 0
lh =0

for idx in range(max_index+1):
    lh = max(lh, storage[idx][1])
    if idx < max_index:
        area += lh * (storage[idx + 1][0] - storage[idx][0])

# 오른쪽에서 최고점부터의 면적 계산
rh = 0
for i in range(n - 1, max_index - 1, -1):
    rh = max(rh, storage[i][1])
    if i > max_index:
        area += rh * (storage[i][0] - storage[i - 1][0])

# 결과 출력
print(area + max_height)  # 최고점의 높이를 더함
