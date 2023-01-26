'''
유람선에는 n 명의 승객
구명보트는 2명 이하 무게 M kg 이하

모두 탈출 구명보트의 최소의 개수
'''

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)
cnt = 0
for idx in range(len(arr)):
    if arr == []:
        break
    elif len(arr) == 1:
        cnt += 1
        break
    elif arr[0] + arr[-1] > m: # 리스트 원소가 한개라면, 2배가 되는 문제가 발생
        arr.pop(0)
        cnt += 1
    else:
        arr.pop() # 엣지 케이스 : 리스트가 1개만 남은경우.. 한개 없애면 빈리스트가 되어서 아래의 경우 오류 발생
        arr.pop(0)
        cnt += 1
print(cnt)

