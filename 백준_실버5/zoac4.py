h, w, n, m = map(int, input().split())

'''
메모리 초과
room = [[False]*w for _ in range(h)]
room[0][0] = True

for row_idx in range(h):
    for col_idx in range(w):
        if room[row_idx][col_idx]:
            try:
                room[row_idx][col_idx + (m+1)] = True
                room[row_idx + (n+1)][col_idx] = True
            except:
                pass

cnt = 0
for row_idx in range(h):
    for col_idx in range(w):
        if room[row_idx][col_idx]:
            cnt +=1

print(cnt)

'''


H, W, N, M = map(int, input().split())

# 각 행과 열에 대해 가능한 참가자 수를 계산
row = H // (N+1) + (1 if H % (N+1) != 0 else 0)
col = W // (M+1) + (1 if W % (M+1) != 0 else 0)

# 가능한 참가자 수를 출력
print(row * col)