import sys

n, m = map(int, input().split())
memo = set()
for _ in range(n):
    memo.add(sys.stdin.readline().rstrip())
for _ in range(m):
    post = set(sys.stdin.readline().rstrip().split(','))
    for i in post:
        memo.discard(i)
    print(len(memo))