'''
플래티넘 11003

최솟값 찾기 1

n 개의 수 와 
l 이 주어진다. (윈도우의 크기)
윈도우에서의 최솟값을 D_i 라 할 때, d 에 저장된 수를 출력하는 프로그램을 작성하시오

시간 복잡도 N 으로 해결해야 하므로

정렬을 사용할 수 없다
'''
from collections import deque
import sys

n, l = map(int, sys.stdin.readline().split())       # 원소의 크기, 윈도우 크기
arr = list(map(int, sys.stdin.readline().split()))  
d = [0 for _ in range(n)]
window = deque()




'''
매번 위도우 위치를 변경할 때마다 Min 함수를 사용하는 경우 
시간 복잡도가 O(n**2) 이 된다.
'''