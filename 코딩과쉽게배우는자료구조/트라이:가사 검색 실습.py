'''
자신이 좋아하는 노래 가사에 사용된 단어들 중 특정 키워드가 몇개 포함되어있는지 프로그램으로 개발

키워드 = 와일트카드 문자 인 ? 가 포함된 패턴 형태의 문자열 (단, ? 는 문자 1개)
        -> 즉 개수도 맞아야 한다.

words : 가사에 사용된 모든 단어 배열(중복 x/ 소문자로만 구성)
queries : 찾고자 하는 키워드가 담긴 배열(중복 가능/ 소문자와 ? 만 구성/ ? 하나이상 포함 (접두 or 접미))

return : 각 키워드 별로 매치된 단어가 몇개인지

words의 단어 개수는 100,000 이하
각 단어의 길이는 10,000 이하
전체 가사 단어 는 1,000,000이하

이 코드는 트라이 자료구조를 이용해 각 길이별로 단어를 저장하고 검색하는 방식을 사용합니다.
 또한, 주어진 쿼리에 대해 매칭되는 단어의 개수를 세는 과정에서, 해당 쿼리에 와일드카드가 있을 때 단어 개수를 셀 수 있는 방법을 이용합니다.

해당 코드의 시간복잡도는 O(NlogN)입니다.
'''

class Node:
    def __init__(self, key):
        self.key = key  # 현재 노드의 문자
        self.cnt = 0  # 현재 노드를 끝으로 하는 단어의 개수
        self.children = {}  # 자식 노드들

class Trie:
    def __init__(self):
        self.root = Node(None)  # 루트 노드
        self.reversed_root = Node(None)  # '?'를 포함한 쿼리를 뒤집어 검색할 루트 노드

    # 단어를 Trie에 삽입하는 함수
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]
            cur.cnt += 1
        return

    # '?'를 포함한 쿼리를 뒤집어 Trie에서 검색하여 매치되는 단어의 개수를 반환하는 함수
    def count(self, query):
        if query[0] == '?':  # 쿼리가 접미사인 경우
            cur = self.reversed_root
            query = query[::-1]
        else:  # 쿼리가 접두사인 경우
            cur = self.root
        for ch in query:
            if ch == '?':  # '?'를 만나면 현재 노드의 단어 개수를 반환
                return cur.cnt
            if ch not in cur.children:
                return 0  # 매치되는 단어가 없음
            cur = cur.children[ch]
        return cur.cnt  # 쿼리에 매치되는 단어의 개수를 반환
    

'''
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word_count = 0
        self.child = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = defaultdict(TrieNode)

    def insert(self, word):
        node = self.root[len(word)]
        node.word_count += 1
        for char in word:
            node = node.child[char]
            node.word_count += 1

    def search(self, query):
        node = self.root[len(query)]
        for i, char in enumerate(query):
            if char == "?":
                return node.word_count
            if char not in node.child:
                return 0
            node = node.child[char]
        return node.word_count

def solution(words, queries):
    answer = []
    tries = [Trie() for _ in range(10001)]
    reversed_tries = [Trie() for _ in range(10001)]
    for word in words:
        tries[len(word)].insert(word)
        reversed_tries[len(word)].insert(word[::-1])
    for query in queries:
        if query[0] == "?":
            answer.append(reversed_tries[len(query)].search(query[::-1]))
        else:
            answer.append(tries[len(query)].search(query))
    return answer
'''