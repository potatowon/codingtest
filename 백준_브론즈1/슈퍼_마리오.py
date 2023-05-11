'''
점수의 합을 최대한 100에 가깝게 만드려고 한다.
'''
import sys
total = 0

for _ in range(10):
    score = int(sys.stdin.readline())
    if total == 0:
        total += score
    elif abs(100 - total) >= abs(100 - (total + score)):
        total += score
    elif abs(100 - total) < abs(100 - (total + score)):
        break
print(total)