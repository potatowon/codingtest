'''
1st 1
2st 2,3,4,5,6,7
3st 8,9,10,11,12,13

13이 들어있는 인덱스는 3 이므로 최소 3개의 방을 지나야 한다.
'''


n = 58 # int(input())

# right -> 1 시작 1, 6, 12, 18씩 커짐
# left -> 1 시작 6씩 커짐
right, left = 1, 1

for idx in range(n//6 + 2):
    if n >= right and n <= left:
        print(idx+1)
        break
    elif idx == 0:
        right = right + 1
        left = left + 6*(idx+1)
    else:
        right = right + idx*6
        left = left + 6*(idx+1)

