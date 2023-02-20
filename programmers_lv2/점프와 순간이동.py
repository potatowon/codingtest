'''
k 칸 앞으로 점프 : 건전지 -K 사용
온거리 * 2 순간이동 : rjswjswl tkdyd ㅌ

순간이동이 효율적, N 만큼 떨어져 있는 장소로 가려고 한다.
점프 이동 최소

N 이 주어졌을때

사용해야하는 건전지 사용량의 최솟값을 return 하시오

2로 나누어 떨어지면 순간이동 하고 아니면 1칸씩 이동한다고 생각하자
'''

def solution(n):
    cnt = 1
    while n != 1:
        if n%2 != 0:
            cnt += 1
            n //= 2
        else:
            n //= 2
    return cnt

print(solution(6))


'''
2로 나눈 나머지를 생각하고 있다 -> 이진법과 같은내용이다 나머지가 존재한다는것은 이진수로 변환했을때 1의 개수와 같다

def solution(n):
    return bin(n).count('1')
'''

