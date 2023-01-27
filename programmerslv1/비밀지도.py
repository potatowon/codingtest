'''
지도는 n*n 정사각형 공백과 # 벽으로 이뤄져 있다.

2장 중 적어도 하나가 벽이면 벽이다.
-> 벽인 부분은 이진수의 1 배열이다.
'''
# print(bin(9)[2:])
'''
n자리에 맞춰서 지도를 만들어야 한다.
'''
def solution(n, arr1, arr2):
    arr = '0'*n
    b1 = [bin(i)[2:] for i in arr1]
    bin1 = ["0"*(n-len(s)) + s if len(s) < n else s for s in b1]
    # print(bin1)
    b2 = [bin(j)[2:] for j in arr2]
    bin2 = ["0" * (n - len(s)) + s if len(s) < n else s for s in b2]
    # print(bin2)
    result = []
    for s1, s2 in zip(bin1, bin2):
        print(s1, s2)
        answer = ''
        for i, j in zip(s1, s2):
            print(i,j)
            if (i == '1') or (j == '1'):
                answer += '#'
            else:
                answer += ' '
        result.append(answer)
    return result
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

print(bin(20|1))