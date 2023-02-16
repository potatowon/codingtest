'''
농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어져 있다. (N is always odd.)
수확시 다이아 몬드 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨둔다.
'''
''' 다맞음 '''
import sys

N = int(input())
data = []
for _ in range(N):
    d = list(map(int, sys.stdin.readline().split()))
    data.append(d)
k = N//2
apples = 0
for idx in range(k):
    a = sum(data[idx][k-idx:k+1+idx])
    b = sum(data[2*k-idx][k-idx:k+1+idx])
    c = a+b
    apples += c
apples += sum(data[k])

print(apples)