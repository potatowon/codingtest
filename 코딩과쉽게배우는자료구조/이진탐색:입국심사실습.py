def solution(n, times):
    left = min(times)
    right = max(times)*n

    while left <= right:
        mid = (right + left) // 2
        checked = 0
        # 심사 가능한 인원수 = 소요시간//심사관당 소요시간
        for i in times:
            checked += mid // i
            if checked >= n:
                break

        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(6, [7, 10]))