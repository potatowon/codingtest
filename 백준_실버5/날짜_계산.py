'''
(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
1년은 111 년
2년 222
3년 333
...

15년 15 15 15
16년 1 16 16
19년 4 19 19
n  15나 28나 19나

'''
e, s, m = map(int, input().split())
earth = [15] + list(range(1, 16))
sun = [28] + list(range(1, 29))
moon = [19] + list(range(1, 20))
num = 1
while True:
    if earth[num%15] == e and sun[num%28] == s and moon[num%19] == m:
        break
    num += 1

print(num)
