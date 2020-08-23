from Tree import Tree

# import sys
# x, opt, y = map(str, sys.stdin.readline().strip().split(' '))
# with open('czy_input1.txt', 'r') as f:
#     tree = map(int, f.readline().strip().split(' '))

# root = Tree(tree[0])

# def read_tree(root, idx):
#     if root == None:
#         return
#     if idx < len(tree):
#         if tree[idx] == -1:
#             root.left = None
#         else:
#             root.left = Tree(tree[idx])
#     else:
#         root.left = None
#     idx += 1
#     if idx < len(tree):
#         if tree[idx] == -1:
#             root.left = None
#         else:
#             root.right = Tree(tree[idx])
#     else:
#         root.left = None
#     read_tree(root.left, idx)
#     read_tree(root.right, idx)
#     return


root = Tree(1, left=Tree(2), right=Tree(3, left=Tree(4)))


# Class Tree(object):
#     def __init(val, left=None, right=None):
#         self.val = val
#         self.left= left
#         self.right = right


def cengcibianli(root):

    output = [[root]]
    current_layer = 0
    while len(output[current_layer]) != 0:
        output.append([])
        for node in output[current_layer]:
            if node.left:
                output[-1].append(node.left)
            if node.right:
                output[-1].append(node.right)

        current_layer += 1

    output.pop()
    for idx, line in enumerate(output):
        output[idx] = map(lambda x: x.val, line)
    return output


# read_tree(root, idx=1)
print cengcibianli(root)














