# 기존 이진 트리에 탐색 함수를 추가


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # 삽입 ( 루트 노드 기준 작으면 좌, 크면 우)
    def insert(self, value):
        new_node = Node(value)

        # 루트 노드 시작
        if self.root is None:
            self.root = new_node
            return
        
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value < value: # 루트노드 보다 큰 경우
                if curr_node.right is None:
                    curr_node.right = new_node
                    break
                curr_node = curr_node.right
            else:                       # 루트 노드보다 작은 경우
                if curr_node.left is None:
                    curr_node.left = new_node
                    break
                curr_node = curr_node.left
    
    # search 
    def has(self, value):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value ==  value:
                return True
            
            if curr_node.value < value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

        return False
    

## result

tree = BinarySearchTree()
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(5)
tree.insert(6)
tree.insert(2)

print(tree.has(6))
print(tree.has(19))
