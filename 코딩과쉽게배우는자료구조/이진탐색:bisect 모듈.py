## 모듈을 이용한 이진탐색 ##

import bisect

arr = [1, 1, 5, 124, 400, 599, 1004, 2876, 8712]

print(bisect.bisect_right(arr, 599)) # 6
print(bisect.bisect_left(arr, 599))  # 5

# bisect_left : 두번째 파라미터를 넣을 수 있는 가장 왼쪽의 Index를 찾는다(즉, 같은 값의 경우 앞쪽으로)
# bisect_right : 가장 오른쪽의 Index (즉, 같은 값이면 뒤쪽으로 index)
    # bisect 와 right 는 동일하게 작동한다.


## 다음과 같이 함수를 만들 수 있다.

def search(arr, value):
    index = bisect.bisect_left(arr, value)
    return index if arr[index] == value else -1