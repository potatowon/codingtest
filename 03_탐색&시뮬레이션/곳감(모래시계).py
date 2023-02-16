'''
감을 깍아 마당에 말리고 있다 마당은 N*N 격자판

각 격자 단위로 말리는 감의 수를 정한다.

회전 정보 (행번호, 방향, 횟수)
0 : 왼쪽
1 : 오른쪽

N is always odd
'''

'''
자연수 N
N*N의 격자
M (1~10)
M 개의 회전 명령
'''
''' 반만 맞음 '''
import sys

N = int(input())
data = []
for _ in range(N):
    d = list(map(int, sys.stdin.readline().split()))
    data.append(d)

M = int(input())
'''
인덱스 사용해서 밀기! 
    주의 사항 list의 길이보다 더 많이 미는 경우
    r = number%len(list) 를 해주어야 오류가 안난다~~ 
'''

for _ in range(M):
    order = list(map(int, sys.stdin.readline().split()))
    if order[1] == 0:
        r = order[2]%N
        new_data = data[order[0]-1][r:] + data[order[0]-1][:r]
        data[order[0]-1] = new_data

    elif order[1] == 1:
        r = order[2]%N
        new_data = data[order[0]-1][-r:] + data[order[0]-1][:-r]
        data[order[0]-1] = new_data
# for d in data:
#     print(d)
'''
pop 을 이용해 밀기
1) 왼쪽
a = [1,2,3,4,5]
b = a.pop(0) 을 하면 1이 pop 되고 a= [2,3,4,5] 가 된다 이때
a.append(b) 를이용해 다시 더해주면
a = [2,3,4,5,1] 왼쪽으로 한 번 민 꼴이 되었다 

for _ in range(k):
    b = a.pop(0)
    a.append(b)
2) 오른쪽 밀기
a = [1,2,3,4,5]
b = a.pop() # 5 -> a = [1,2,3,4]
# 여기서 문제는 0번째 인덱스에 집어 넣는것이다. 
a.insert(0, b) 를 이용한다.
a = [5, 1, 2, 3, 4]
따라서 오른쪽 밀기

for _ in range(k):
    b = a.pop()
    a.insert(0, b)
    
  
'''

# 합산
k = N//2
apples = 0
for idx in range(k):
    a = sum(data[idx][idx:N-idx])
    b = sum(data[2*k-idx][idx:N-idx])
    c = a+b
    apples += c
apples += data[k][k]

print(apples)

'''
13
55 51 76 47 59 21 44 82 28 35 55 11 49
41 49 47 74 22 64 57 72 46 100 53 67 73
75 45 25 48 55 49 40 25 20 79 19 96 94
62 29 99 84 10 35 14 68 52 25 92 45 90
2 92 67 10 67 71 30 31 81 8 25 68 54
65 52 16 93 90 84 58 65 48 46 22 40 19
86 39 28 87 5 42 54 28 65 62 33 48 77
86 5 13 33 48 92 38 15 84 10 38 85 36
76 11 41 41 68 70 27 66 95 56 57 43 100
62 61 81 11 96 62 60 28 30 40 97 55 9
49 49 83 57 52 6 74 11 61 48 45 16 21
59 80 74 4 71 64 79 24 3 79 68 24 58
4 32 52 91 43 93 59 65 51 98 78 67 42
5
1 0 3
10 1 9
3 0 11
5 0 25
3 1 11
'''
''' 4956 '''