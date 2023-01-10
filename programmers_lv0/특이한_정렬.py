# 특이한 정렬.py

'''
정수 n 을 기준으로 n과 가까운 수부터 정렬
거리가 같다면 큰수가 앞으로 오게 정렬
'''
# a = [1,2,3,4,10,7,23]
# a = sorted(a, key=lambda x : abs(x-4))
# print(a)
def solution(numlist, n):
    result = sorted(numlist, key=lambda x : abs(x-n))
    for idx in range(len(result)):
        if abs(n-result[idx]) == abs(n-result[idx-1]):
            result[idx-1], result[idx] = max(result[idx], result[idx-1]), min(result[idx], result[idx-1])

    return result

print(solution([10000,20,36,47,40,6,10,7000], 30))