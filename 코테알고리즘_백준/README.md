## 📌 시간복잡도를 고려하는 방법
- N 의 최댓값을 고려하여 O(N) 인지, O(NlogN)을 사용하면 좋을지 고려하는 것이 좋다.
- `sorted`의 시간 복잡도 $O(NlogN)$
- - list의 sum 함수의 시간 복잡도 $O(N)$

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

## 📌 투 포인터
2개의 포인터로 알고리즘의 시간 복잡도를 최적화 하자.  
투포인터의 경우는 포인터를 어디서 시작할지에 대한것을 고민하는 것이 중요하다.
- 💻 투포인터 구현의 기본
```
start = 0
end = n-1
while start < end:
```

- 대표예제 : 프로그래머스(숫자의 표현), 백준(연속된 자연수의 합)
비슷한 방식으로 문제를 풀이 하였으나 백준은 메모리 초과 되는 현상 발생

- `range`에서 메모리 초과가 되는것 같다. 리스트를 사용하는 방식 주의 
```
def solution(n):
    numbers = [i for i in range(n+1)]

    start_idx, end_idx = 1, 1
    cnt = 1


    while end_idx != n:
        sum_ = sum(numbers[start_idx:end_idx+1])

        if sum_ == n:
            cnt += 1
            end_idx += 1
        elif sum_ < n:
            end_idx += 1
        else:
            start_idx += 1
    return cnt

```

```
import sys

n = int(sys.stdin.readline())


start_idx, end_idx = 1, 1       # 투 포인터 초기화
cnt = 1                         # 자기 자신을 포함하므로 고려 하여 초기화
sum_ = 1


while end_idx != n:

    if sum_ == n:
       cnt += 1
       end_idx += 1
       sum_ += end_idx
    elif sum_ < n:
        end_idx += 1
        sum_ += end_idx
    else:
        sum_ -= start_idx
        start_idx += 1

print(cnt)
```

## 📌 슬라이딩 윈도우
1. 2개의 포인터로 범위를 지정한다.
2. 범위를 유지한채로 이동을 하면서 문제를 해결한다.
3. 투 포인터 알고리즘과 비슷한 개념과 원리를 지녔다.

## 📌 스택과 큐

### 스택
- 후입 선출로 이루어진 자료구조
    - append
    - pop()

> 파이썬의 스택
위치
- top : 삽입과 삭제가 일어나는 위치  

연산
- 너비 우선 탐색에서 자주 사용하므로 스택과 함께 잘 알아두어야 하는 개념이다.
- `s.append(data)` : 삽입
- `s.pop()` : 삭제

### 큐
- 선입 선출로 이루어진 자료 구조 
    - append
    - popleft()

