# 📌 원본에서 만들기
- 원래의 데이터 행렬에서 `상하좌우`에 추가하는 방법

```python
import sys

a = [list(map(int, sys.stdin.realine().split())) for _ range(n)] # n 행의 갯수

# 0 행 0만 가진 행의 추가
a.insert(0, [0]*n)
# 마지막 행 0만 가진 행의 추가
a.append(0, [0]*n)

# 각 행의 처음과 마지막에 0 추가
for x in a:
  x.insert(0 ,0)
  x.append(0)
  
```

# 📌 새로운 보드를 만들고 그안에 원본 데이터를 넣는 방식
- 원본데이터 보다 Pad 만큼 증가한 새 board 를 만들고 추가하는 방식

```python

data = [list(map(int, sys.stdin.realine().split())) for _ range(n)] # n 행의 갯수

board = [[0 for _ in range(n+2)] for _ in range(n+2)] # pad=1  인 경우

# board의 기존 데이터 삽입하기
for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] = data[i-1][j-1]
        
```

## 🔥 level up 깊은 복사와 얕은 복사
- 프로그래머스 Lv0 : 행렬의 연산
- 프로그래머스 Lv0 : 안전지대

### 1차원 배열에서 배열을 선언
1차원에서의 배열의 선언은 `*`을 통해 쉽게 선언할 수 있다.

```python
row = 10
arr = [0]*row

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
### 2차원 배열에서의 배열의 선언
😞 틀린 방법 
```python
row = 10
col = 5

arr = [[0]*col]*row

[[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]
```
문제없이 생성이 되는 듯 하나, 해당 array의 `0행 0열` 하나 변경하면 모든 행의 0열의 값이 변한다.<\br>
`*`을 이용해 배열을 선언하게 되면, **얕은 복사(shallow copy)** 가 진행되어 배열 내 모든 원소들이 같은 저장소의 값을 가지게 되고<\br>
따라서 요소를 변경하면 다른 요소들의 값도 바뀌는 것이다. 

🔥 해결!
```python

rows = 10
cols = 5
arr = [[0 for j in range(cols)] for i in range(rows)]



