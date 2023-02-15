'''
알파벳 소문자로만 이루어진 단어 S 알파펫이 단어 몇개가 포함
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = [0]*len(alphabet)

s = input()

for i in s:
    res[alphabet.index(i)] += 1
print(*res)