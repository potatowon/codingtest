## 📌 구간 합
구간 합 알고리즘을 활용하려면 먼저 합 배열을 구해야한다.

> ⏰ 시간복잡도
$O(N)$ 에서 $O(1)$ 로 감소한다

### 1차원의 합 배열
- 합 배열 S 의 정의
```
1차원의 경우
S[i] = A[0]+A[1]+A[2]+A[3] ... + A[i-1]+A[i]

-> 합 배열은 기존의 리스트 데이터를 전처리한 배열이라 생각하면 된다.
```
- 1 차원 배열합 구하는 방법
> 😞 LV1

```
numbers # 수열
for i in numbers:
    tmp += i
    prifix_sum.append(tmp)
```

> 🔥 LV2
```
A # 기존 수열
S = [0]*n
S[0] = A[0]
for i in range(1, n):
    S[i] =  S[i-1] + A[i]
```

### 2차원의 합 배열
1. 2차원 배열 합 만드는 법 -> (1,1) 기준으로하는 배열합 기준을 만든다
```
A # 주어진 배열
D =[[0]*(n+1) for _ in range(n+1)] # 합 배열 초기화
# N*N 기준 - matrix
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

```
2. 배열합을 기준으로 하여 계산한다.  -> (x1, y1)~(x2, y2)


```
result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
```

📑 백준 11660번
```

import sys

n, m = map(int, sys.stdin.readline().split(' '))
matrix = [[0]*(n+1)]
for _ in range(n):
    row = [0] + list(map(int, sys.stdin.readline().split(' ')))
    matrix.append(row)
# 2차원 배열 합 만들기

D =[[0]*(n+1) for _ in range(n+1)] # 합 배열 초기화

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + matrix[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
```


