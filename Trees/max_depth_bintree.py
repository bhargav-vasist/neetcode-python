# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            # this takes a snapshot of the current state of the queue before we append shit to it
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def maxDepthStackBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        lvl = 0
        while stack:
            node, depth = stack.pop()
            if node:
                lvl = max(lvl, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return lvl

    maxDepth = maxDepthStackBFS
