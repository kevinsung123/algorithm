import sys


class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


def preorder(node):
    print(node.parent, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.parent, end='')
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.parent, end='')


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    tree = {}
    for i in range(N):
        p, l, r = sys.stdin.readline().split()
        tree[p] = Node(p, l, r)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])