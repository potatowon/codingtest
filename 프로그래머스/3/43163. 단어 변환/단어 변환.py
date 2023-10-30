def is_one_diff(word1, word2):
    if len(word1) != len(word2):
        return False
    diff_cnt = sum([1 for a, b in zip(word1, word2) if a!=b])
    return diff_cnt == 1

def dfs(words, start, target, visited):
    if start == target:
        return 0

    answer = float('inf')  # 무한대로 초기화
    visited[start] = True
    for w in words:
        if (not visited[w]) and (is_one_diff(start, w)):
            answer = min(answer, 1 + dfs(words, w, target, visited))
    visited[start] = False

    return answer

def solution(begin, target, words):
    if target not in words:
        return 0

    visit = {w: False for w in words}
    visit[begin] = False
    answer = dfs(words, begin, target, visit)
    return answer if answer != float('inf') else 0
