'''
연속하는 20일중 10일동안만 사용할 수 있다.

연속하는 8일 중 5일 동안만 사용할수 있다 20일짜리 휴가를 시작 => 14일

'''

import sys
cnt = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())

    if all(i == 0 for i in (l,p,v)):
        break
    else:
        print(f'Case {cnt}: {(v//p)*l + min((v%p),l)}')
        cnt += 1