'''
N개의 수로 된 수열이 있다. 이 수열의 i~j 까지의 합이 M 이 되는 경우의 수를 구하는 프로그램
'''



''' run time error'''
import sys
#
# N, M = map(int, sys.stdin.readline().split()) # N개로 된 수열의 합이 M 이 되는 배열 찾기
#
# numbers = list(map(int, sys.stdin.readline().split()))
# cnt = 0
# for i in range(N):
#     if numbers[i] == M:
#         cnt += 1
#     for j in range(N):
#         if sum(numbers[i:j]) == M :
#            cnt += 1
#
# print(cnt)


'''
n 개의 수열에서 연속적인 부분합이 m 이 되게 하는 경우의 수
'''

'''
lt, rt 리스트를 가리키는 포인터
tot 는 연속된 수열의 합 < M 합이 작으면 rt 포인터 이동
                   = M 같으면 카운트 -> lt 이동, tot 에 기존 lt 값 삭제 
                   > M 크면 lt 포인터의 이동
tot = a[0]

lt = 0 
rt = 1
-> rt가 가르키는 바로 앞 인덱스까지의 합

'''
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)