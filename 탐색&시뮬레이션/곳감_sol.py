import sys
# sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
for x in a:
    print(x)
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
'''
13
55 51 76 47 59 21 44 82 28 35 55 11 49
41 49 47 74 22 64 57 72 46 100 53 67 73
75 45 25 48 55 49 40 25 20 79 19 96 94
62 29 99 84 10 35 14 68 52 25 92 45 90
2 92 67 10 67 71 30 31 81 8 25 68 54
65 52 16 93 90 84 58 65 48 46 22 40 19
86 39 28 87 5 42 54 28 65 62 33 48 77
86 5 13 33 48 92 38 15 84 10 38 85 36
76 11 41 41 68 70 27 66 95 56 57 43 100
62 61 81 11 96 62 60 28 30 40 97 55 9
49 49 83 57 52 6 74 11 61 48 45 16 21
59 80 74 4 71 64 79 24 3 79 68 24 58
4 32 52 91 43 93 59 65 51 98 78 67 42
5
1 0 3
10 1 9
3 0 11
5 0 25
3 1 11
'''