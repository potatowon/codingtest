import sys
s = 'i'
while s != '#':
    s = sys.stdin.readline().strip()
    vowel = 'aeiou'
    vowel = vowel + vowel.upper()
    cnt = 0
    if s == '#':
        break
    for i in s:
        if i in vowel:
            cnt += 1
    print(cnt)