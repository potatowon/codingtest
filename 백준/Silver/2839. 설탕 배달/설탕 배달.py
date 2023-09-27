n = int(input())
cnt = 0
possible = False
while n >= 0:
    if n % 5 == 0:
        cnt += n//5
        possible = True
        break
    n -= 3
    cnt += 1

if possible:
    print(cnt)
else:
    print(-1)

