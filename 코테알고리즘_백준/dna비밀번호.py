## 실버5 , 129891

'''
dna = {'A','C','G','T'}

# dna의 문자열의 길이, 부분 문자열의 길이
# dna 문자열
# acgt의 최소 개수
'''


import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().strip()
checklist = list(map(int, input().split()))
checklist = {"A":checklist[0], "C":checklist[1], "G":checklist[2], "T":checklist[3]}
mylist = {"A":0, "C":0, "G":0, "T":0}
cnt = 0
## 처음 윈도우의 개수
window = dna[:p]
for d in window:
    mylist[d] += 1
if all(mylist[i] >= checklist[i] for i in 'ACGT'):
    cnt += 1
## 1단계씩 증가하는 경우
for i in range(1, s-p+1):
    mylist[dna[i-1]] -= 1
    mylist[dna[i+p-1]] += 1
    if all(mylist[i] >= checklist[i] for i in 'ACGT'):
        cnt += 1

print(cnt)


        
'''
코멘트

처음 윈도우의 개수에 대한 딕셔너리를 저장한 후에
윈도우가 옮겨지면서 모든 문자열에 대한 개수를 다시 저장하는 것이 아닌
제거되는 문자열의 개수를 하나 줄이고
추가 되는 문자열의 개수를 하나 증가시키는 방법으로 계산하였다.

이때 윈도우의 총 개수는 s-p+1 임을 항상 기억하자
'''