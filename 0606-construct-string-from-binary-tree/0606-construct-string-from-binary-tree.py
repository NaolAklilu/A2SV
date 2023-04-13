# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def tree(node):
            if node == None:
                return []
            else:
                curString = [str(node.val)]
                leftBranch = tree(node.left)
                curString.append("(")
                curString.extend(leftBranch)
                curString.append(")") 

                rightBranch = tree(node.right)
                
                if rightBranch:
                    curString.append("(")
                    curString.extend(rightBranch)
                    curString.append(")")

                return curString
            
        string = tree(root)        
        ans = []
        for i in range(len(string)):
            if string[i] == ")":
                if ans[-2] == "(" and ans[-1]==")":
                    ans.pop()
                    ans.pop()
            ans.append(string[i])
            
        if ans[-2] == "(" and ans[-1]==")":
            ans.pop()
            ans.pop()

        return "".join(ans)
                
                
                
                
               
            