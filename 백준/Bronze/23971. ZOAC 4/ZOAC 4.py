H, W, N, M = map(int, input().split())

# 각 행과 열에 대해 가능한 참가자 수를 계산
row = H // (N+1) + (1 if H % (N+1) != 0 else 0)
col = W // (M+1) + (1 if W % (M+1) != 0 else 0)

# 가능한 참가자 수를 출력
print(row * col)