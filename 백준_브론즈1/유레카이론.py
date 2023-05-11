'''
모든 자연수는 최대 3개의 삼각수의 합으로 표현할 수 있다. ==> 유레카 이론

자연수가 주어졌을때 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 여부에 대한 판단

ex) 4, 6은 삼각수의 합으로 표현 할수 없다.
표현 할 수 있으면 1, 아니면 0을 출력하라.
'''
import sys

# 삼각수 배열
triangular_number = [(i*(i+1))//2 for i in range(1, 46)]
eureka_num = [False, True, True] + [False]*998

for i in triangular_number:
    for j in triangular_number:
        for k in triangular_number:
            if i + j + k <= 1000:
                eureka_num[i+j+k] = True

t = int(input())

for _ in range(t):
    k = int(sys.stdin.readline())
    if eureka_num[k]:
        print(1)
    else:
        print(0)