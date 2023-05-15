N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]

row = [0]*N
col = [0]*M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = row.count(0)
col_count = col.count(0)

print(max(row_count, col_count))
