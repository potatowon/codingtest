'''
같은 눈 3개 10000 + 눈*1000
2개 1000 + 같은눈*100
가장큰눈 * 100
'''

s, t, r = map(int, input().split(' '))

if s == t and t == r:
    p = 10000 + s*1000
elif s == t or t == r or s == r:
    if s == t:
        p = 1000 + s * 100
    elif t == r:
        p = 1000 + t * 100
    elif s == r:
        p = 1000 + r * 100
else:
    p = max(s, t, r)*100
print(p)