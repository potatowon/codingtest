n = int(input())
data = list(map(int, input().split()))
line = [0] * n

for i in range(1, n + 1):  # 키가 1부터 N까지
    cnt = 0
    for j in range(n):
        if cnt == data[i - 1] and line[j] == 0:  # cnt가 data[i-1]과 같고, line[j]가 비어있으면
            line[j] = i  # line[j]에 i를 삽입
            break
        elif line[j] == 0:  # line[j]가 비어있으면 cnt 증가
            cnt += 1

print(' '.join(map(str, line)))
