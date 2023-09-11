import sys

n, m = map(int, input().split())
titles = []

def binary_search(titles, score):
    l, r = 0, len(titles) - 1
    while l <= r:
        mid = (l + r) //2
        if titles[mid][1] < score:
            l = mid + 1
        else:
            r = mid - 1

    return l


for _ in range(n):
    name, score = sys.stdin.readline().split()
    titles.append((name, int(score)))
titles.sort(key=lambda x : x[1])

for _ in range(m):
    score = int(sys.stdin.readline())
    name = binary_search(titles, score)
    print(titles[name][0])
