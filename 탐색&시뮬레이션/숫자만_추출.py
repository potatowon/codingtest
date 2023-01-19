''' 문자열과 숫자가 주어진 경우 숫자만 추출하여 순서대로 자연수를 만든다. 단 0 이 맨 앞이면 안된다.'''

import sys
#
s = sys.stdin.readline().strip()
num = []
for i in s:
    if i.isdigit(): # int('0028') = 28 이므로 앞에있는 0을 걸러주는 과정이 필요가 없다.. 괜
        if int(i) == 0:
            if len(num) != 0:
                num.append(i)
        else:
            num.append(i)
answer = ''.join(num)
division = []
for j in range(1, int(answer)+1):
    if int(answer)%j == 0:
        division.append(j)
print(int(answer))
print(len(division))

# for i in s:
    # if i.isdigit():
        #num.append(i)
# answer = int(''.join(num))


''' 앞에 나오는 0 거르는 방법  00243 이라면
res = res*10 + int(x) 0을넣어도 res는 계속 0 이므로 걸러짐 2 부터 값이 들어간다 처음 24 -> 240 + 3 이런식으로'''
