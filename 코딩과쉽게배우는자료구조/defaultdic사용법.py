'''
defaultdic 은 dic 함수와 달리 value의 초기값을 제공한다.
'''

## values 를 숫자 0 으로 초기화 하기

from collections import defaultdict

d = defaultdict(int)
names = ['Lee', 'James', 'John', 'Smith', 'Lee', 'James']
for name in names:
    d[name] += 1

print(d)

## 원하는 유형으로 초기화 가능하다!! 

from collections import defaultdict

list_dict = defaultdict(list)
list_dict['key'] += [1, 3, 5]
print(list_dict) # [1, 3, 5]

set_dict = defaultdict(set)
set_dict['key'].update((1, 3, 5, 3, 2, 8))
print(set_dict) # {1, 2, 3, 5, 8} 

dic_dict = defaultdict(dict)
dic_dict['key']['name'] = 1
print(dic_dict) 

### tuple 에 대해서 튜플은 값을 변화시킬 수 없기때문에.. 굳이 튜플로 초기화 .. 할 필요가 없다
# 되는지 안 되는지는 할 필요 없어서 안해보았다.