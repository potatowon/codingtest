'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중 s번째(s-1) 부터 e번째까징의 수를 오름차순 정렬 k 번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요
'''

# def solution(T, s, e, k):
#     result = T[s-1: e]
#     result.sort()
#     return result[k-1]



import sys

T = int(input())
# answer = []
for _ in range(T):
    N, s, e, k = map(int, sys.stdin.readline().split())
    lis = list(map(int, sys.stdin.readline().split()))
    result = lis[s-1:e]
    result.sort()
    # answer.append(result[k-1])
    print(result[k-1])