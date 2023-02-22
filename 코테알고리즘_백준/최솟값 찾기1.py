'''
플래티넘 11003

최솟값 찾기 1

n 개의 수 와 
l 이 주어진다. (윈도우의 크기)
윈도우에서의 최솟값을 D_i 라 할 때, d 에 저장된 수를 출력하는 프로그램을 작성하시오

시간 복잡도 N 으로 해결해야 하므로

정렬을 사용할 수 없다
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
A = list(map(int, input().split()))
A = [A[0]]*(l-1) + A
## 시작

