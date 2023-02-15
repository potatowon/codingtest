'''
원섭, 세희 상근, 숭, 강수 5명
40 미만 40 점
   이상 그대로

'''

import sys
scores = []
for _ in range(5):
    scores.append(int(sys.stdin.readline()))

print(sum([n if n >= 40 else 40 for n in scores])//5)