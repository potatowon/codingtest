'''
1. n*n 크기의 비어있는 2차원 배열을 만든다
2. i 행 i열까지 i 로 채우기
3. 모든 행을 각가 잘라내어 모두 이어 붙인 새로운 1차원 배열
4. left~riGht까지 남기고 나머지 지우기
'''

# def solution(n, left, right):
#     arr = []
#     # for i in range(n):
#     #     arr += [i+1]*i + list(range(i+1,n+1))
#     # return arr[left:right+1]

# def solution(n, left, right):
#     arr_n = [[]*n for _ in range(n)]
#
#
'''
규칙 각 좌표에 채워지는 수는 n행, m열 에서 그 수가 큰 값이다.

--> 1줄로 배열을 변경한다 

5이면 총 5*5개의 배열이 생김 
13인덱스(14번째수) 라면 행열로 바꾸게 되었을때 --> 3행 4열의 수 

13%5+1 열
13//5+1 행 
  
'''
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = (i//n) + 1
        col = (i%n) + 1
        answer.append(max(row, col))
    return answer
# print(solution(3, 2, 5))

