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


for k in range(n):              # 각 num의 모든 원소를 돌아야 하므로, 인덱스 설정
    tmp = num[:k] + num[k+1:]   # 자기 자신의 인덱스를 제외함.
    i, j = 0, len(tmp)-1        # 포인터를 양끝에서 부터 시작 -> 초기화
    while i < j:
        t = tmp[i] + tmp[j]     # 포인터 두 수의 합
        if t == num[k]:         
            cnt += 1            # 좋은 수를 만족하는 경우 수 증가 후 break
            break
        elif t < num[k]:        # num이 정렬 되어 있으므로, t 값이 작으면 왼쪽 포인터 증가
            i += 1
        else:
            j -= 1              # 수가 크면 오른쪽 인덱스 감소
        
print(cnt)
