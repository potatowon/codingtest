'''
아나그램 : 나열 순서는 다르지만 그 구성이 일치 하는 경우


두 문자가 주어지면 아나그램인지 판별하는 프로그램을 작성하시오
단, 대소문자가 구분 됩니다.

YES, NO


'''

import sys
from collections import defaultdict


word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()

word1_dic = defaultdict(int)
word2_dic = defaultdict(int)


for s in word1:
    word1_dic[s]

for i in word2:
    word2_dic[i]

if word1_dic == word2_dic:
    print("YES")
else:
    print("NO")

    

