'''
버거 + 음료 - 50

상덕, 중덕, 하덕
콜라 사이다


'''
import sys
buger = []
soda = []
for _ in range(3):
    buger.append(int(sys.stdin.readline()))
for _ in range(2):
    soda.append(int(sys.stdin.readline()))

print(min(buger)+min(soda)-50)