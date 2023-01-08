# 종이 자르기
'''가로길이가 M 이면 M-1 번자르고
세로길이가 N 이면 (N-1)*N 자른다'''

def solution(M,N):
    return (M-1) + (N-1)*M

print(solution(2,2))
print(solution(1,1))
print(solution(2,5))