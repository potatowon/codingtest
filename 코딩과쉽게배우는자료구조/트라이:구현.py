# 트라이 구조는 해시테이블과 연결 리스트를 사용한다.

class Node:
    def __init__(self, value = ""):
        self.value = value
        self.children = dict() # 간선은 키로 받는다.

class Trie:
    def __init__(self):
        self.root = Node()      # 루트 노드는 비어있다.

    
    def insert(self, string):
        curr_node = self.root       # 루트 노드에서 시작.

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(curr_node.value + char)
            curr_node = curr_node.children[char]

    def has(self, string):
        curr_node = self.root

        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

trie = Trie()
trie.insert('cat')
trie.insert('can')

print(trie.has('can'))
print(trie.has('cat'))
print(trie.has('cap'))