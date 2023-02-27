'''
시에쓰일단어를 미리 노트에적어둡니다.

N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다. -> 찾기
3<= k <= 100
n 개의 단어
n-1 의 단어

'''

import sys
# from collections import deque

n = int(sys.stdin.readline())
word = [sys.stdin.readline().strip() for _ in range(n)]
use_word = [sys.stdin.readline().strip() for _ in range(n-1)]

for i in use_word:
    if i in word:
        word.remove(i)

print(*word)
