t = int(input())
table = []
for _ in range(t):
    s, e = map(int, input().split())
    table.append((s, e))
cnt = 0
table.sort(key=lambda x : (x[1], x[0]))
end = 0

for use in table:
    if end <= use[0]:
        start = use[0]
        end = use[1]
        cnt += 1
print(cnt)