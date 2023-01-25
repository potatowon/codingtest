
# 0125
'''
K 개의 랜선을 잘라  -> N개의 같은 길이의 랜선
1. 이미 잘린 랜선은 이어서 사용할 수 없다
2. 자를 때는 정수 배로 자른다
3. 기존의 K 개의 랜선으로 N 개의 랜선을 만들 수 없다
4. N 개 보다 많이 만드는것도 N 개를 만드는 것에 포함 된다.
5. 만들 수 있는 최대의 랜선 길이를 구하는 프로그램
'''

'''
이미 가지고 있는 랜선의 갯수 K , 필요한 랜선의 갯수 N
K 줄에 걸쳐 이미 가지고 있는 랜선의 길이가 주어진다. 

'''

# 이분검색 : 결정알고리즘 방법론에서 사용
## 특징) 특정 범위 안에 답이 있다는 걸 알 수 있다
## 그러면 거기서 답을 정하고 이분 검색을 이용하여 그 값이 답으로서 유효한지 아닌지 판단.
### 답이 되면 범위를 좁힌다. -> 더 좋은 답을 향해 줄여나감.
import sys

K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
start = 0
end = max(arr)

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for i in arr:
        n = i//mid
        cnt += n
    if cnt >= N:
        break
    else:
        end = mid - 1
print(mid)

