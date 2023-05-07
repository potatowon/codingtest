import sys

tmp = []

for _ in range(5):
    tmp.append(sys.stdin.readline().rstrip())

answer = ''

for i in range(15):
    for s in tmp:
        try:
            answer += s[i]
        except:
            pass

print(answer)