import sys

n, t = sys.stdin.readline().split()
mini_game = {'Y': 2, "F": 3, "O": 4}
user = set()
for _ in range(int(n)):
    id = sys.stdin.readline().rstrip()
    user.add(id)
print(len(user) // (mini_game[t]-1))
