import sys
from collections import defaultdict

n = int(input())
cards = defaultdict(int)

for i in list(map(int, sys.stdin.readline().split())):
    cards[i] += 1
m = int(input())
for j in list(map(int, sys.stdin.readline().split())):
    print(cards[j], end=' ')