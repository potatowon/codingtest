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

# for i in use_word:
#     if i in word:
#         word.remove(i) # remove 는 시간복잡도가 N 이므로 시간 초과 가능성
#                         # Hash 테이블 이용하기

check_dic = {}

for i in word:
    check_dic[i] = 1 # 정해진 word에 대해 1 값
for i in use_word:
    check_dic[i] = 0 # 사용한 단어는 0으로 초기화 -> 사용하지 않은건 1로 남아있음

for k,v in check_dic.items():
    if v == 1:
        print(k)
        break

# print(*word)
