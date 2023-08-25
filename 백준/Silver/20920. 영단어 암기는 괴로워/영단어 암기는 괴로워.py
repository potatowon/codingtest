# 실버 3 영단어 암기는 어려워.py

import sys
from collections import defaultdict

N, M = map(int, input().split())
words = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        words.append(word)

words_dic = defaultdict(int)
for i in words:
    words_dic[i] += 1

res = sorted(words_dic.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))
for k, v in res:
    print(k)
