N = int(input())
arr = list(map(int, input().split()))
S = int(input())

i = 0
while i < N-1 and S > 0:
    max_idx = i
    for j in range(i+1, N):
        # 현재 S 내에서 swap 가능하고, 숫자가 크면 갱신
        if j - i <= S and arr[j] > arr[max_idx]:
            max_idx = j

    # max_idx 위치의 숫자를 앞으로 가져옴
    while max_idx > i:
        arr[max_idx], arr[max_idx - 1] = arr[max_idx - 1], arr[max_idx]
        max_idx -= 1
        S -= 1
    i += 1

print(*arr)
