'''
이 문제는 트라이(Trie) 자료구조를 사용하여 해결할 수 있지만, 이 코드는 이진 탐색(Binary Search)을 사용하여 해결합니다.

우선, 가사 단어들을 단어의 길이에 따라 분류하여 저장합니다. 이때, 저장한 가사 단어들은 정렬된 상태로 저장합니다. 왜냐하면 이후 이진 탐색을 사용할 것이기 때문입니다.

그 다음, 검색 키워드를 하나씩 가져와서 다음과 같이 처리합니다.

검색 키워드의 첫 글자가 '?'가 아니라면, 이 검색 키워드와 길이가 같은 가사 단어들 중에서 검색 키워드와 일치하는 단어의 개수를 이진 탐색을 통해 찾습니다. 이때, '?'를 'a'로 바꾼 문자열과 'z'로 바꾼 문자열을 이진 탐색에 사용합니다. 이는 '?'가 어떤 문자에도 매치된다는 성질을 이용한 것입니다.

검색 키워드의 첫 글자가 '?'이라면, 이 검색 키워드와 길이가 같은 가사 단어들을 거꾸로 저장한 배열에서 검색 키워드와 일치하는 단어의 개수를 이진 탐색을 통해 찾습니다. 이때, 검색 키워드를 뒤집어서 처리합니다. 예를 들어, 검색 키워드가 '?rodo'라면, 거꾸로 저장한 배열에서는 'odor?'와 같은 형태로 저장되어 있기 때문입니다.

마지막으로, 각 검색 키워드마다 찾은 단어의 개수를 answer에 저장하여 반환합니다.
'''

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    for query in queries:
        if query[0] != '?':
            res = count_by_range(arr[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
