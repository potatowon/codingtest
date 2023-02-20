'''
주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면
그 수를 좋은 수 라고 한다. N개의 수 중 좋은 수가 몇개 인지 구하시오
'''

n = int(input())
num = list(map(int, input().split(' ')))
# n = 10
# num = [1,2,3,4,5,6,7,8,9,10]
num.sort()
cnt = 0


for k in range(n):
    tmp = num[:k] + num[k+1:] # 자기 자신의 인덱스를 제외함.
    i, j = 0, len(tmp)-1
    while i < j:
        t = tmp[i] + tmp[j]
        if t == num[k]:
            cnt += 1
            break
        elif t < num[k]:
            i += 1
        else:
            j -= 1
        
print(cnt)
