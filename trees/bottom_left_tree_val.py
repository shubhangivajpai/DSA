# Find bottom left tree value

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        left_most=root.val
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                if i==0:
                    left_most=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left_most

        
