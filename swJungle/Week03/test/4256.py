import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class TreeNode:
    def __init__(self,val,leftchild=None,rightchild = None):
        self.val = val
        self.leftchild = leftchild
        self.rightchild = rightchild


def generate_tree(pre_order,in_order):
    if len(pre_order) == 0 :
        return
    elif len(pre_order) == 1:
        return TreeNode(pre_order[0])

    root = TreeNode(pre_order[0])
    idx = in_order.index(root.val)
    left_subtree = generate_tree(pre_order[1:idx+1],in_order[:idx])
    right_subtree = generate_tree(pre_order[idx+1:],in_order[idx+1:])
    root.rightchild = right_subtree
    root.leftchild = left_subtree

    return root


def post_order(tree):
    if tree.leftchild:
        post_order(tree.leftchild)
    if tree.rightchild:
        post_order(tree.rightchild)
    print(tree.val,end=" ")






for _ in range(int(input())):

    n = int(input())

    pre_order = list(map(int,input().split()))
    in_order = list(map(int,input().split()))

    tree = generate_tree(pre_order,in_order)

    post_order(tree)
    print()