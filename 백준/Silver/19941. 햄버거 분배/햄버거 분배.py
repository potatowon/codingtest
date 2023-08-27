N, K = map(int, input().split())
table = list("O"*K + input().rstrip() + "O"*K)
cnt = 0
for idx in range(K, len(table)-K):
    if table[idx] == "P":
        windows = table[idx-K: idx+K+1]
        for jdx, manu in enumerate(windows):
            if manu == "H":
                table[jdx + (idx - K)] = "E"
                cnt += 1
                break
# print(table)
print(cnt)


