## 까먹지 말자 sort 의 default 값은 오름차순

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(A[K-1])