N = int(input()) # 굴다리의 길이
M = int(input()) # 가로등의 개수
X = [0] + list(map(int, input().split())) + [N] # 가로등의 좌표

max_d = 0
# 시작과 첫 번째 가로등 간의 거리
max_d = max(max_d, X[1])

# 마지막 가로등과 굴다리의 끝 간의 거리
max_d = max(max_d, N - X[-2])

# 가로등 사이의 거리 계산
for idx in range(2, len(X)):
    max_d = max(max_d, (X[idx] - X[idx-1] + 1) // 2)

print(max_d)
