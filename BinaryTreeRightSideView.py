class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()

                # Add the last node in this level
                if i == level_length - 1:
                    result.append(node.val)

                # Queue the children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
