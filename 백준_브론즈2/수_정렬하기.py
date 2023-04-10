import sys


n = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(n)]
# 입력되는 숫자가 커지면 메모리가 커짐
numbers.sort() # 시간복잡도 O(nlogn)
# 데이터의 양을 고려하면 for문 한개로 해결해야함.
for i in numbers:
    print(i)