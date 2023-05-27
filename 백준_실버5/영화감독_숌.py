n = int(input())
idx = 1
num = 666
while True:
    if n == idx:
        break
    num += 1
    if str(num).count('666') >= 1:
        idx += 1

print(num)