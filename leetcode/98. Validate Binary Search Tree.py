class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def dfs(curr):
            if not curr:
                return None
            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)
        dfs(root)
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True
