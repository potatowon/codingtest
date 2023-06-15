import sys

n = int(input())
stack = set()

for _ in range(n):
    name, access = sys.stdin.readline().split()
    if access == 'enter':
        stack.add(name)
    else:
        stack.discard(name)
stack = list(stack)
stack.sort(reverse=True)
for n in stack:
    print(n)