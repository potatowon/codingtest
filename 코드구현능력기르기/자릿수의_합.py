'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 합이 최대힌 자연수를 출력하라
'''

import sys

N = int(input())
numbers = list(sys.stdin.readline().split())
result = []
for num in numbers:
    total = sum([int(i) for i in num])
    result.append(total)

idx = result.index(max(result))
print(numbers[idx])

