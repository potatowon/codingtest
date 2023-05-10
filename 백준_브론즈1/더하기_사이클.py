
num = input().strip()
cnt = 0

new_num = num
answer = ''
if int(num) < 10 :
    new_num = num + '0'

while answer != num:
    sum_ = str(sum([int(i) for i in new_num]))
    answer = new_num[-1] + sum_[-1]
    new_num = answer

    cnt += 1
    if int(answer) == int(num) and cnt > 1:
        break

if int(num) < 10 :
    print(cnt-1)
else:
    print(cnt)


