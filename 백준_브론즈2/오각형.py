'''
n 단계의 점의 개수는 모두 몇개인가'?
'''

N = int(input())
answer = 5
for i in range(1, N):
    answer += 3*i+4

print(answer%45678)