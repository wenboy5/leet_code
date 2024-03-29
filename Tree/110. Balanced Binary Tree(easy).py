'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_height(self,root):
            if root == None:
                return 0
            else:
                return 1 + max(self.find_height(root.left), self.find_height(root.right))
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        else:
            return abs(self.find_height(root.left)-self.find_height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right) 
                
            