
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        # Use recursion to solve the problem as the iterative approach was logic-heavy
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively call invertTree on the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
