class Node():
    def __init__(self, top = -1):
        self.top = top
        self.nodes_left = 0
        self.left = None
        self.right = None
        self.value = None

    def __str__(self):
        if self.left is None:
            return f" Top: { self.top };  value: { self.value }; nodes left: { self.nodes_left }; left: { self.left }; right: { self.right } "
        else:
            return f" Top: { self.top }; value: { self.value }; left: { self.left.value }; right: { self.right.value }; nodes left: { self.nodes_left } "


def solution(h, q):
    tops = dict()
    
    def create_tree(node : Node, height : int, nodes_left : int) -> None:
        if height == 0:
            return
        
        node.value = 2 ** height - 1 + nodes_left

        if node.value in q:
            tops[node.value] = node.top

        node.left = Node(top = node.value)
        create_tree(node.left, height - 1, nodes_left = node.nodes_left + nodes_left)
        node.nodes_left = (0 if node.left.value is None else (node.left.nodes_left + 1))

        node.right = Node(top = node.value)
        create_tree(node.right, height - 1, nodes_left = node.nodes_left + nodes_left)
        node.nodes_left += (0 if node.right.value is None else (node.right.nodes_left + 1))
    
    root = Node()
    create_tree(root, h, 0)

    res = []
    for el in q:
        res.append(tops[el])

    return res

    
print(solution(5, [19, 14, 28]))


