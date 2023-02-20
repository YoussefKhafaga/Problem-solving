class Solution(object):
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        q = []
        q.append(root)
        while len(q) is not 0:
            curr = []
            for i in range(0, len(q)):
                node = q.pop(0)
                curr.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(curr)
        return res