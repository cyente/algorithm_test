# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        output = []

        def copy_tree(root1, root2):
            if root2:
                root1 = TreeNode(root2.val)
            else:
                return
            copy_tree(root1.left, root2.left)
            copy_tree(root1.right, root2.right)

        def gentree(node, start, ended, root):
            if start > ended:
                temp_root = None
                copy_tree(temp_root, root)
                print temp_root
                print root
                output.append(temp_root)
            for idx in range(start, ended + 1):
                node = TreeNode(idx)
                gentree(node.left, start, idx - 1, root)
                gentree(node.right, idx + 1, ended, root)

        for idx in range(1, n + 1):
            root_node = TreeNode(idx)
            gentree(root_node.left, 1, idx - 1, root_node)
            gentree(root_node.right, idx + 1, n, root_node)
        return output

a = Solution()

print(a.generateTrees(10))

