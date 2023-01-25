'''
임의의 N 개의 숫자가 주어질때, N 개의 오름차순으로 정렬한 다음 -> 그 중 한개의 수인 M이 주어지면 이분 검색으로 M 정렬된 상태에서 몇번쨰 있는지 구하는 프로그램
단, 중복값은 존재하지 않는다.
'''
# 결정알고리즘 방법론에서 사용 -> 특정 범위안에 답이 있다는 걸 알 수 있다.
import sys


N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
length = len(numbers)
start = 0
end = length - 1
while start <= end:
    mid = (start + end)//2
    if numbers[mid] == M:
        break
    elif numbers[mid] > M:
        end = mid - 1

    else:
        start = mid + 1
print(mid + 1)