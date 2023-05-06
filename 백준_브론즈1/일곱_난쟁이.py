'''
난쟁이의 키의 합이 100이됨.
--> 9명 중 7난쟁이 찾기
'''

import sys
import itertools
tall = []
for _ in range(9):
    tall.append(int(sys.stdin.readline()))

C = itertools.combinations(tall, 7)

lst = list(C)

for i in lst:
    if sum(i) == 100:
        dwarf = i
dwarf = sorted(list(dwarf))
for d in dwarf:
    print(d)