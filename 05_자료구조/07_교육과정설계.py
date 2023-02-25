'''
총 과목 : A, B, C, D, E, F, G
필수과목 : C, B, A

이 순서대로 계획을 짜야한다 즉 필수과목의 순서를 유지한채로 짜야함

필수 과목이 주어지고 수업설계가 잘되었으면 'YES' 아니면 'NO'를 출력
'''
import sys

subject = sys.stdin.readline().strip()
n = int(input())        # 수업설계의 개수

# subject = 'CBA'
# n = 3
for j in range(n):
    plan = sys.stdin.readline().strip()
    ans = ''
    for i in plan:
        if i=='C' or i=='B' or i=='A':
            ans += i
    if ans == subject:
        print(f'#{j+1} YES')
    else:
        print(f"#{j+1} NO")
