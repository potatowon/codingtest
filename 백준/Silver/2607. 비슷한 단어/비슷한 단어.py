from collections import Counter

def is_similar(word1, word2):
    c1, c2 = Counter(word1), Counter(word2)
    
    # 두 단어의 길이 차이가 2 이상이면 False
    if abs(len(word1) - len(word2)) > 1:
        return False

    # 두 단어의 문자 출현 횟수 차이를 확인
    diff_cnt = 0
    for k, v in c1.items():
        diff_cnt += abs(v - c2.get(k, 0))

    for k, v in c2.items():
        if k not in c1:
            diff_cnt += v

    return diff_cnt <= 2

# 입력 처리
n = int(input())
words = [input().strip() for _ in range(n)]

# 첫 번째 단어와 비슷한 단어 카운트
count = 0
for i in range(1, n):
    if is_similar(words[0], words[i]):
        count += 1

print(count)
