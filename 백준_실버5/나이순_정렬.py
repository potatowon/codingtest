import sys

n = int(input())
members = []

for idx in range(n):
    age, name = sys.stdin.readline().split()
    members.append((idx, int(age), name))

members.sort(key=lambda x : (x[1], x[0]))
for idx, age, name in members:
    print(age, name)
