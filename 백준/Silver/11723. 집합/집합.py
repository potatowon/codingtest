import sys
n = int(input())
s = set()

'''
set 함수의 시간 복잡도 체크 하기
'''

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == 'all' or cmd == 'empty':
        if cmd == 'all':
            s = set(range(1, 21))
        else:
            s = set()
    else:
        x, n = cmd.split()
        n = int(n)
        if x == 'add':
            s.add(n)
        elif x == 'check':
            if n in s:
                print(1)
            else:
                print(0)
        elif x == 'remove':
            s.discard(n)
        elif x == 'toggle':
            if n in s:
                s.discard(n)
            else:
                s.add(n)

