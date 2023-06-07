import sys

P = int(input())
for _ in range(P):
    res = []
    t, *num = map(int, input().split())
    answer = 0
    for i in num:
        res.append(i)
        new_num = sorted(res)
        if new_num != res:
            answer += len(new_num[new_num.index(i)+1:])
        res.sort()
    print(t, answer)

## 출력 형식을 찾자.. 하.. t 안써서 6번을 틀림.

# a = [900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919]
# b =[901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 900]
#
# print(a!=b)