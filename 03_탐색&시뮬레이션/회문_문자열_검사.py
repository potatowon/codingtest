'''
N 개의 문자열을 입력 받아 앞에서 읽을 때나 뒤에서 읽을때가 같은 회문 문자열의 경우
단, 대소문자를 구분하지 않는다
YES / NO
'''

import sys

N = int(input())

for i in range(1, N+1):
    string = sys.stdin.readline().strip()
    string = string.lower() # 대소문자를 구분하지 않기 때문에 (대문자 Or 소문자로 바꿔주는 과정이 필요하다)
    reverse_string = string[::-1]
    if string == reverse_string:
        answer = "YES"
    else:
        answer = "NO"
    print(f"#{i} {answer}")
