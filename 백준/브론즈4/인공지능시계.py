h, m, s = map(int, input().split(' '))
d = int(input())
new_s = s + d
if new_s//60 >= 1:
    m += new_s//60
    new_s %= 60
    if m//60 >= 1:
        h += m//60
        m %= 60
        if h >= 24:
            h %= 24
    print(h, m, new_s)
else:
    print(h, m, new_s)