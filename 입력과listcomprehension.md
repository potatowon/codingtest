코드 구현 능력 기르기
## 📌 코딩테스트에서 입력받기
한 두줄 입력 받지 않고 `for`문을 통해 여러줄을 `input`을 통해 입력 받는 경우 -> 시간초과가 발생할 수 있다.
### 💡 sys.stdin.readline() 이용하기
1. 한개의 정수를 입력 받는 경우
```python
import sys
a = int(sys.stdin.readline()
```
  이때 `int` 를 사용하는 것은 -> 문자열로 인식 되기 때문이다.
2. 여러개의 정수를 띄어쓰기를 통해 입력받는 경우
```python
import sys
a, b, c = map(int, sys.stdin.readline().split())
```
```
❓ map(함수, list)
리스트 요소를 지정된 함수로 처리해주는 함수이다
함수의 자리에는 `lambda` 또는 `int`를 자주 사용한다. 
````

3. 여러개의 정수를 list 로 입력 받는 경우
```python
import sys
lst = list(map(int, sys.stdin.readline().split()))
```
> str 값으로 저장할 때는 int를 제외하면 마찬가지 이다.

4. 그대로 str로 사용하는경우
- **주의** 해당 함수로 불러오게 되면 공백문자도 불러오기 때문에 공백문자 제거 과정이 필요하다
- `strip()`사용
```python
s = sys.stdin.readline().strip()
```

## 📌 list comprehension
리스트를 for, if, else 문을 활용하여 한줄로 써보자</br>
💡 for 문만 사용하기
- 형식
```python
lst = [표현식 for 변수 in 리스트]
```
💡 for 문 & if 문
- 형식
```python
lst = [조건 만족시 표현식 if 조건문 for 변수 in 리스트]
```
💡 중첩 for 문
- 형식
```python
lst = [표현식 for 변수1 in 리스트1 for 변수2 in 리스트2]
```
💡 for문, if, else 구문
- 형식
```python
lst = [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data]
```



