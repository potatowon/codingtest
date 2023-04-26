'''
A 만원의 고정비용(매년)
B 만원의 가변비용


노트북 가격 C 만원

수입 > 고정비용 + 가변비용 지점을 손익 분기점
최초로 이익이 발생하는 판매량을 출력한다.
'''


A, B, C = map(int, input().split())

if C - B > 0:
    print(A//(C-B) + 1)
else:
    print(-1)