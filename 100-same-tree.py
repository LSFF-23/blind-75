# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False

s = Solution()
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
assert s.isSameTree(p1, q1) == True, "#1"
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))
assert s.isSameTree(p2, q2) == False, "#2"
p3 = TreeNode(1, TreeNode(2), TreeNode(2))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
assert s.isSameTree(p3, q3) == False, "#3"