'''
1 ~ n 번의 사람들이 끝말 잇기를 하고있다

1. 차례로 단어 말하기
2. 다 끝나면 다시 처음으로
3. 앞선 사람의 단어의 마지막 문자
4. 이전에 등장했던 단어 안됨
5. 한글자 안됨

[가장먼저 탈락한 사람, 몇번째 차례에서 탈락했는지]
탈락자 없는 경우
[0, 0]
'''

def solution(n, words):
    n_cnt = [0]*n
    stack = []
    for i, s in enumerate(words):
        n_cnt[i%n] += 1
        if stack and ((s in stack) or (stack[-1][-1] != s[0])):
            return [i%n+1, n_cnt[i%n]]
        else:
            stack.append(s)
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))




