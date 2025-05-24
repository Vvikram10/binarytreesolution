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

# second way
from collections import deque
from typing import Optional, List
# BFS Approach takesoumen collection 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
