# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def generate(start,end):
            if start > end:
                return [None]
            
        
            trees = []

            for root in range(start,end+1):
                left_trees = generate(start,root-1)
                right_trees = generate(root+1,end)

                for left in left_trees:
                    for right in right_trees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            
            return trees
    
        return generate(1,n)