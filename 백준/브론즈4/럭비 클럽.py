import sys

while True:
    name, age, weight = sys.stdin.readline().split(' ')
    if int(age) > 17 or int(weight) >= 80:
        print(name, 'Senior')
    elif int(age) > 0 and int(weight) > 0:
        print(name, 'Junior')
    else:
        break

