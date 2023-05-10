'''
검색 결과가 주어졌을 때, 어떤 패턴?

알파벳, . ?
'''

import sys

n = int(input())
directory = []
for _ in range(n):
    directory.append(sys.stdin.readline().rstrip())
    n_name = len(directory[0])
